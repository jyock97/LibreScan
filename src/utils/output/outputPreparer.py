import os


class OutputPreparer:

    def __init__(self, p_path):
        self.working_dir = p_path

    def _delete_pics(self):
        delete_pics_file = self.working_dir + "/.toDelete.ls"
        with open(delete_pics_file) as f:
            for filename in f:
                filename = filename[:-1]
                os.remove(self.working_dir + "/processed/" + filename + ".hocr")
                os.remove(self.working_dir + "/processed/" + filename + ".tif")
                os.remove(self.working_dir + "/raw/" + filename + ".jpg")
        f.close()

    def _rename_pics(self):
        rename_pics_file = self.working_dir + "/.pics.ls"
        pic_number = 1
        print(self.working_dir)
        with open(rename_pics_file) as f:
            for filename in f:
                filename = filename[:-1]
                pic_name = self.working_dir + "/processed/" + filename
                new_pic_name = "rlsp" + str(pic_number).zfill(5)
                new_pic_name = self.working_dir + "/processed/" + new_pic_name
                if (os.path.exists(pic_name + ".hocr") and
                        os.path.exists(pic_name + ".tif")):
                        os.rename(pic_name + ".hocr", new_pic_name + ".hocr")
                        os.rename(pic_name + ".tif", new_pic_name + ".tif")
                        pic_number += 1

    def run(self):
        self._delete_pics()
        self._rename_pics()
