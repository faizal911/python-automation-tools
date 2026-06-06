# try:
#     filename = input("enter filename:")
#     with open(filename,"r")as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("file not found.please check the filename")
# finally:
#     print("operation completed")    

#   ----------------------------------------------------------

# def check_marks(marks):

#     if marks<0:
#         raise ValueError('marks cannot be negative')
    
#     if marks>100:
#       raise ValueError("marks cannot be greater then 100")   
#     print("valid marks:",marks) 
  
# try:
#         check_marks(75)
# except ValueError as e:
#         print("error:",e)

# try:
#      check_marks(-10)
# except ValueError as e:
#      print("error:",e)  

# try:
#      check_marks(150)
# except ValueError as e:
#      print("errer",e)         

#   ----------------------------------------------------------
