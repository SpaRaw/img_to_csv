try:
    import numpy as np

except ImportError as e:
    print("numpy is not installed")

try:
    from PIL import Image
except ImportError as e:
    print("PIL is not installed")

try:
    import csv
except ImportError as e:
    print("csv is not installed")




def main():

    path = input("Pfad zum Bild")

    img = Image.open(path)

    img_arr = np.array(img)
    img_arr = np.reshape(img_arr, (-1, 3))

    with open("output.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(img_arr)





if __name__ == "__main__":
    main()