from pathlib import Path
import pickle
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import sys

def main(argv):
    ppt_file = Presentation(argv[0])
    irasutoya_count = 0
    aseets_path = Path(Path(__file__).parents[1], 'assets')
    save_path = Path(aseets_path, 'irasutoya.pickle')
    
    with open(save_path, 'rb') as irp:
        irstya_list = pickle.load(irp)
        irstya_title_list = [title for (title, _) in irstya_list]
        irstya_img_list = [img_name for (_, img_name) in irstya_list]
        
    for slide in ppt_file.slides:
        for shape in slide.shapes:
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                ppt_img_name = shape._pic.nvPicPr.cNvPr.get('descr')
                if (ppt_img_name in irstya_title_list) or (ppt_img_name in irstya_img_list):
                    irasutoya_count += 1
                    
    print("The number of your slide is {}.".format(irasutoya_count))
    if irasutoya_count > 20:
        print("If this slide is for commercial purpose, you must keep within 20 irasutoya products.")
                
                
if __name__ == "__main__":
    main(sys.argv[1:])