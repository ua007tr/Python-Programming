import csv 

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number", "E-Mail ID"])
        
        writer.writerow(info_list)
        
if __name__ == '__main__':
    condition = True

    student_num = 1

    while(condition):
        student_info = input("Enter students information or students {} in the following format (NAME AGE CONTACT_NUMBER E-MAIL_ID): ".format(student_num))

        student_info_list = student_info.split(" ")
        print("the entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-Mail_ID: {} " 
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is the entered information correct ? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information of anther students:")            
            if condition_check == "yes":
                write_into_csv(student_info_list)
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check =="no":
            print("\nPlease re-enter the values ")

Output Jupyter:-

  Enter students information or students 1 in the following format (NAME AGE CONTACT_NUMBER E-MAIL_ID): Aswin 18 659812 Aswin@gm.com
  the entered information is -
  Name: Aswin
  Age: 18
  Contact_Number: 659812
  E-Mail_ID: Aswin@gm.com 
  Is the entered information correct ? (yes/no): yes
  Enter (yes/no) if you want to enter information of anther students:yes
  Enter students information or students 2 in the following format (NAME AGE CONTACT_NUMBER E-MAIL_ID): Sia 19 13265 Sia@ya.com
  the entered information is -
  Name: Sia
  Age: 19
  Contact_Number: 13265
  E-Mail_ID: Sia@ya.com 
  Is the entered information correct ? (yes/no): yes
  Enter (yes/no) if you want to enter information of anther students:yes
  Enter students information or students 3 in the following format (NAME AGE CONTACT_NUMBER E-MAIL_ID): Tanya 20 879655 Tanya@re.com
  the entered information is -
  Name: Tanya
  Age: 20
  Contact_Number: 879655
  E-Mail_ID: Tanya@re.com 
  Is the entered information correct ? (yes/no): yes
  Enter (yes/no) if you want to enter information of anther students:no
  
Output in MS Excel Sheet:-

Name	  Age	  Contact Number	E-Mail ID
Aswin	  18	  659812	        Aswin@gm.com
Sia	    19	  13265	          Sia@ya.com
Tanya	  20	  879655	        Tanya@re.com
			
