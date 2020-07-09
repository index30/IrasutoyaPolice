from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import sys

def main(argv):
    ppt_path = Path(Path.cwd().parent, "ppt_file", argv[0])
    ppt_file = Presentation(ppt_path.as_posix())
    for slide in ppt_file.slides:
            for shape in slide.shapes:
                if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                    print(shape._pic.nvPicPr.cNvPr.get('descr'))
                
if __name__ == "__main__":
    main(sys.argv[1:])