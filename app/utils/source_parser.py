import re
from typing import List

from app.configs.source_aware_labels import SOURCE_LABELS, COMMON_LABELS
from app.pydantics.document_chunks import RawDocument ,Section
def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def first_sentences(text: str, n: int = 2) -> str:
    text = normalize_text(text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(parts[:n]).strip() if parts else text[:300]


def get_labels_for_source(source_type:str) -> List[str]:
    labels = SOURCE_LABELS.get(source_type.lower(), [])
    return list(dict.fromkeys(COMMON_LABELS + labels))


def parser(doc:RawDocument) -> List[Section]:
    source = doc.source_type.lower()
    
    if source == "confluence":
        return parse_confluence(doc.content)
    if source == 'slack':
        return ''
    if source == 'gmail':
        return ''
    return [Section(section_title= doc.title or 'content', content= normalize_text(doc.content))]
    
def parse_confluence(content:str) -> List[Section]:
    lines= normalize_text(content).split("\n")
    sections: List[Section]=[]
    current_title = "root"
    current_lines: List[str]=[]
    heading_re = re.compile(r"^(#{1,6})\s+(.*)$")
    
    for line in lines:
        m= heading_re.match(line.strip())
        print(m, '-----heaing')
        
        
        
        if m:
            if current_lines:
                sections.append(
                    Section(
                        section_title=current_title,
                        content=normalize_text("\n".join(current_lines))
                    )
                )
            current_title = m.group(2).strip()
            current_lines=[]
        else:
            current_lines.append(line)
         
    if current_lines:
        sections.append(
            Section(
                section_title=current_title,
                content= normalize_text("\n".join(current_lines))
            )
        )
        
    # print("-------------")
    # print(sections) 
    
    return sections
                     
        
    