from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json

# updated this program to save the file in json format

# password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['1','2','3','4','5','6','7','8','9','0']

    symbols = ['!','@','#','$','%','^','&','*','(',')','{','}','|','?','>','<','[',']',':',';','"',',','.','/','~','_','+','=','-']


    letters_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for i in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list  = letters_list + symbol_list + number_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    password_entry.insert(0, password)
    pyperclip.copy(password)   # it copies the string to clipboard
# print(password)

# save password
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email": email,
        "password": password
    }}

    if len(website)<1 or len(password)<1:
        messagebox.showwarning(title='Oops', message='Please don\'t leave any of the fields empty')
    else:
        # with open('data.json', 'r') as data:
        #     # json.dump(new_data, data, indent= 4)  # used to write in json file 
        #     # read_data = json.load(data)    # to read the data and it converts it to dict
        #     # print(read_data)
            
        #     # updating the data
        #     # step 1 - read the data
        #     read_data = json.load(data)
        #     # step 2 - update the data
        #     read_data.update(new_data)
        #     # step 3 - write/save the updated data
        # with open('data.json', 'w') as data:
        #     json.dump(read_data, data, indent= 4)
        
        # modify the above code with try except 
        try:
            with open('data.json', 'r') as data:  
                read_data = json.load(data)
        except FileNotFoundError:
            with open('data.json', 'w') as data:  
                json.dump(new_data, data, indent=4)
        else:
            read_data.update(new_data)
            with open('data.json', 'w') as data:
                json.dump(read_data, data, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            
def search():
    user_query = website_entry.get()
    try:
        with open('data.json', 'r') as data:
            read_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message="No data file found")
    else:
        if user_query in read_data:
            email = read_data[user_query]['email']
            password = read_data[user_query]['password']
            messagebox.showinfo(title= user_query, message= f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Oops', message= f'No details for the {user_query} exists')

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50 )


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file= 'logo.png')
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)

website_label = Label(text= "Website:")
website_label.grid(row=1, column=0)

username_label = Label(text= 'Email/Username:')
username_label.grid(row=2 , column=0)

password_label = Label(text= "Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=30)
website_entry.focus()     # this function helps in taking the cursor to entry as soon as the app is run
website_entry.grid(row=1, column=1,)

username_entry = Entry(width=50)
username_entry.insert(0,'abc@gmail.com')
username_entry.grid(row=2, column=1,columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2 )

search_button = Button(text='Search', command=search, width=15)
search_button.grid(row=1, column=2 )

add_button = Button(text= 'Add', width=45, command= save_password)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()

# import pandas as pd
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter, landscape
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, BaseDocTemplate, Frame, Paragraph
# from reportlab.lib.units import inch
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.graphics.shapes import Drawing, Line
# from reportlab.graphics import renderPDF
 
# def merge_cells(data, columns_to_merge):
#     merged_data = data.copy()
#     for col in columns_to_merge:
#         last_value = None
#         last_possession_ref = None
#         merge_start = 0
   
#         for i in range(len(data)):
#             current_value = data.at[i, col]
#             current_possession_ref = data.at[i, 'Possession Ref']
#             if col == 'Possession Ref':
#                 if current_value == last_value:
#                     merged_data.at[i, col] = ""
#                 else:
#                     if i > merge_start:
#                         merged_data.at[merge_start, col] = f'{merged_data.at[merge_start, col]}|{i - merge_start}'
#                     last_value = current_value
#                     merge_start = i
#             else:
#                 if current_value == last_value and current_possession_ref == last_possession_ref:
#                     merged_data.at[i, col] = ""
#                 else:
#                     if i > merge_start:
#                         merged_data.at[merge_start, col] = f'{merged_data.at[merge_start, col]}|{i - merge_start}'
#                     last_value = current_value
#                     last_possession_ref = current_possession_ref
#                     merge_start = i
#         if merge_start < len(data):
#             merged_data.at[merge_start, col] = f'{merged_data.at[merge_start, col]}|{len(data) - merge_start}'
#     return merged_data
 
# def create_pdf(data, colors_dict, output_filename):
#     page_width = len(data.columns) * 100
#     page_height = 800

#     pdf = BaseDocTemplate(output_filename, pagesize=(page_width, page_height),
#                           rightMargin=inch/2, leftMargin=inch/2, topMargin=inch/2, bottomMargin=inch/2)
#     styles = getSampleStyleSheet()
#     header_style = styles['Normal']
#     header_style.alignment = 1

#     frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height - inch, id='normal')


#     def header(canvas, doc):
#         canvas.saveState()

#         canvas.setFont("Helvetica-Bold", 10)
#         canvas.drawString(inch/2, page_height - inch, "Network Rail")
#         canvas.drawCentredString(page_width / 2.0, page_height - inch, "EAS Section-7")
#         canvas.drawRightString(page_width - inch/2, page_height - inch, "Data Freeze: EAS_V_2_2023")

#         canvas.drawString(inch/2, page_height - inch - 12, "HS1 Route")
#         canvas.drawCentredString(page_width / 2.0, page_height - inch - 12, "Version 2.0")
#         canvas.drawRightString(page_width - inch/2, page_height - inch - 12, "Previous Freeze: EAS_V_1_2023")

#         drawing = Drawing(page_width, 20)
#         line = Line(0, 0, page_width - pdf.leftMargin - pdf.rightMargin, 0)
#         line.strokeColor = colors.black
#         drawing.add(line)
#         renderPDF.draw(drawing, canvas, pdf.leftMargin, page_height - inch - 24)

#         canvas.restoreState()

#     template = PageTemplate(id='test', frames=frame, onPage=header)
#     pdf.addPageTemplates([template])

#     table_data = [list(data.columns)]
#     spans = []

#     # Define paragraph styles for highlighting
#     highlight_blue_style = ParagraphStyle('highlight_blue', backColor=colors.blue, textColor=colors.black, alignment=0, leftIndent=3, rightIndent=3)
#     highlight_orange_style = ParagraphStyle('highlight_orange', backColor=colors.orange, textColor=colors.black, alignment=0, leftIndent=3, rightIndent=3)
#     highlight_green_style = ParagraphStyle('highlight_green', backColor=colors.green, textColor=colors.black, alignment=0, leftIndent=3, rightIndent=3)

#     highlight_styles = {
#         1: highlight_blue_style,
#         2: highlight_orange_style,
#         3: highlight_green_style,
#     }

#      # Define default style for handling NaN flags
#     highlight_default_style = ParagraphStyle('highlight_default', alignment=0, leftIndent=3, rightIndent=3)
    
#     for row_index, row in data.iterrows():
#         table_row = []
#         for col_index, value in enumerate(row):
#             cell_value = str(value).split("|")[0] if "|" in str(value) else str(value)
#             flag = colors_dict.get((row_index, col_index), None)
#             if flag:
#                 para = Paragraph(cell_value, highlight_styles.get(flag, highlight_default_style))
#                 table_row.append(para)
#             else:
#                 table_row.append(cell_value)
            
#             # Handle cell spans
#             if "|" in str(value):
#                 actual_value, span = value.split("|")
#                 span = int(span)
#                 spans.append(('SPAN', (col_index, row_index + 1), (col_index, row_index + span - 1)))

#         table_data.append(table_row)



#     table = Table(table_data, repeatRows=1)
#     # added
#     #  # Calculate the maximum width of content in each column
#     # column_widths = [max(len(str(value)) for value in data[col]) for col in data.columns]

#     # # Set column widths dynamically based on the maximum content width
#     # column_widths = [(i, width * 10) for i, width in enumerate(column_widths)]  # Convert to suitable units

#     # # Create the table data with dynamic column widths
#     # table_data_with_widths = [[Paragraph(str(value), styles['Normal']) if isinstance(value, str) else value for value in row] for row in data.values]

#     # # Create the table with dynamic column widths and updated data
#     # table = Table(table_data_with_widths, repeatRows=1, colWidths=[width for _, width in column_widths])

#     font_size = 8

#     style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#                         ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#                         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                         ('BACKGROUND', (0, 1), (-1, -1), colors.white),
#                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#                         ('FONTSIZE', (0, 0), (-1, -1), font_size)] + spans)
    
    
#     table.setStyle(style)
#     pdf.build([table])

# def main():
#     excel_file = "Mock Data Final_v2 2 6.xlsx"
#     sheet_name = "Sheet1"
#     columns_to_keep = ["Possession Ref", "LOR", "Possession Location from", "Possession Location to", "Blocked Line", "Protection Type", "Start Date", "End Date", "Traffic Remarks", "Work Type"]
#     columns_to_merge = ["Possession Ref", "LOR", "Traffic Remarks", "Work Type"]
#     flag_columns = ["Possession Ref_Flag", "LOR_Flag", "Possession Location from_Flag", "Possession Location to_Flag", "Blocked Line_Flag", "Protection Type_Flag", "Start Date_Flag", "End Date_Flag", "Traffic Remarks_Flag", "Work Type_Flag"]

#     try:
#         data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=columns_to_keep + flag_columns)
#     except FileNotFoundError:
#         print(f"Error: File {excel_file} not found.")
#         return
#     except Exception as e:
#         print(f"Error reading Excel file: {e}")
#         return

#     colors_dict = {}
#     for col in columns_to_keep:
#         flag_col = col + "_Flag"
#         for i, flag in enumerate(data[flag_col]):
#             if flag:
#                 colors_dict[(i, columns_to_keep.index(col))] = flag


 
#     data = data[columns_to_keep]
#     data = merge_cells(data, columns_to_merge)
 
#     output_pdf = "Output_New_merge.pdf"
#     create_pdf(data, colors_dict, output_pdf)
#     print(f"PDF created successfully: {output_pdf}")
 
# if __name__ == "__main__":
#     main()