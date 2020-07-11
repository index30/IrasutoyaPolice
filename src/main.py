from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import sys

def main(argv):
    ppt_file = Presentation(argv[0])
    for slide in ppt_file.slides:
        for shape in slide.shapes:
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                print(shape._pic.nvPicPr.cNvPr.get('descr'))
                
if __name__ == "__main__":
    main(sys.argv[1:])