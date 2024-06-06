from wired_table_rec import WiredTableRecognition


table_rec = WiredTableRecognition()

img_path = "0.jpg"
table_str, elapse = table_rec(img_path)
print(table_str)
print(elapse)

# from lineless_table_rec import LinelessTableRecognition
#
# engine = LinelessTableRecognition()
#
# img_path = "0.jpg"
# table_str, elapse = engine(img_path)
#
# print(table_str)
# print(elapse)