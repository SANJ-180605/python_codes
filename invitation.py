def main():
  # print("enter your names")
  names=[]
  while True:
    name=input("enter the names : ")
    if name=="":
      break
  names.append(name)
  # user_input=input("enter names with space after each name:")
  # names=user_input.split()
  # print("list of the names:",names)
  # #names=["Sanju","bhavu","chandu"]
  for name in names:
    print(write_letter(name,"Basavachary"))

def write_letter(reciever,sender):
  return f"""
  ------------------------------
  dear {reciever},

  you are cordially invited to a ball in this evening at 7pm

  sincerely,
  {sender}
  ------------------------------
  """

main()