import pandas as pd
import os
import shutil
from tqdm import tqdm

cwd = os.getcwd()
def upper_folder():
    folders , paths = scan_dir("./all_data")
    df = pd.read_excel("ID.xlsx", engine="openpyxl")
    for i in tqdm(range(len(folders))):
        sdf = df[(df['Folder Name']=='{}'.format(folders[i])) & (df['AAPP ID'].str.len() > 0) ].copy()
        print(f"Path : {paths[i]}")
        ## rename column
        sdf.rename(columns={'Image filenames (with .jpg extension)':'Image_names'}, inplace=True)
        # ## remove unnecessary columns
        sdf = sdf[['AAPP ID', 'Image_names']]
        print(f"{folders[i]} : Shape : {sdf.shape}")
        ## create dict from dataframe
        s_dict = {key: tuple(value.values()) for key,value in sdf.set_index('Image_names').to_dict('index').items()}
        # print(sdf.head())
        rename_move(s_dict, paths[i])
        ## test value print
        # print(list(s_dict)[0])
        print("----x----")
    print("All subfolders finished!")

def rename_move(s_dict,directory):
    path = f"{cwd}/Output"
    try:
        os.chdir(f'{directory}/')
        print(f"Inside : {os.getcwd()}")
    except:
        print("Something wrong with Directory!")
    finally:
        print("Restoring Path")
        os.chdir(cwd)
        print(f"Default dir: {os.getcwd()}")
        os.chdir(f'{directory}/')
        print(f"Retry dir : {os.getcwd()}")
    
    for count,file in enumerate(os.listdir()):
        print(f"Count : {count}")
        if file.endswith("jpg") and s_dict.get(file) != None:
            f_name, f_ext = os.path.splitext(file)
            # print(f_name,"-",f_ext)
            id = s_dict[file][0]
            new_name = f"{id}{f_ext}"
            print(f"Old name {f_name} replaced with New name : {new_name}")
            os.rename(file, new_name)
            shutil.move(new_name, '{}/{}'.format(path,new_name))
        else:
            print("Value not contain!")
            pass
    print("Rename success!")

def scan_dir(dirname) -> list:
    subfolder = [f.name for f in os.scandir(dirname) if f.is_dir()]
    subpath = [f.path for f in os.scandir(dirname) if f.is_dir()]
    return list(subfolder),list(subpath)
        

if __name__ == "__main__":
    upper_folder()