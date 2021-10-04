from PyQt5 import QtWidgets, uic
import sys
import res_rc
from random import randrange
import datetime
import ast
import math

class record:
    def __init__(self):
        
        self.start_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.finish_time = 0
        self.question = []
        self.correct_answer = []
        self.answer_provided = []
        self.isCorrect = []

    def get_output_string(self):
        output = []
        output.append(str(self.start_time))
        output.append(str(self.finish_time))
        output.append(self.question)
        output.append(self.correct_answer)
        output.append(self.answer_provided)
        output.append(self.isCorrect)
        return str(output)

class menu_ui(QtWidgets.QMainWindow):
    #get records
    def __init__(self):
        self.max_round = 5
        self.records = []

        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi("menu.ui", self)
        self.setWindowTitle('Multiplication Challenge')
        self.show()

        start_button = self.pushButton
        start_button.clicked.connect(self.start_click)
        self.pushButton_2.clicked.connect(self.performance)

    def get_records(self):
        self.records = []
        try:
            with open('records.txt', 'r') as f:
                for line in f:
                    if line != "\n":
                        self.records.append(ast.literal_eval(line))
        
        except:
            self.records = []

    def performance(self):
        self.get_records()
        self.ui = uic.loadUi("performance.ui", self)
        self.setWindowTitle('Multiplication Challenge')
        self.label_12.setText(str(self.get_number_of_records()))
        if self.get_number_of_records() != 0:
            self.label_11.setText(str(self.get_average_score()) + " / " + str(self.max_round))
            self.label_8.setText(str(self.get_average_time()) + " seconds")
        else:
            self.label_11.setText("0 / " + str(self.max_round))
            self.label_8.setText("0 seconds")
        self.show()
        self.pushButton_6.clicked.connect(self.restart)
        self.pushButton_7.clicked.connect(self.details)

    def get_number_of_records(self):
        return len(self.records)

    def get_average_score(self):
        sum = 0
        for data in self.records:
            sum = sum + data[5].count(True)
        return round(sum / self.get_number_of_records(),2)

    def get_average_time(self):
        date_format_str = "%d/%m/%Y %H:%M:%S"
        time = 0
        for data in self.records:
            start = datetime.datetime.strptime(data[0], date_format_str)
            end = datetime.datetime.strptime(data[1], date_format_str)
            time = time + self.get_time_diff(start, end)
        return round(time / self.get_number_of_records(),2)


    def get_time_diff(self, start, end):
        time_diff = end - start
        return time_diff.total_seconds()
        

    def details(self):
        self.ui = uic.loadUi("details.ui", self)
        self.setWindowTitle('Multiplication Challenge')
        self.table_representation()
        self.show()
        self.pushButton_6.clicked.connect(self.restart)
        self.pushButton_7.clicked.connect(self.performance)

    def table_representation(self):
        date_format_str = "%d/%m/%Y %H:%M:%S"
        for data in self.records:
            time_diff = self.get_time_diff(datetime.datetime.strptime(data[0], date_format_str), datetime.datetime.strptime(data[1], date_format_str))
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
            self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
            self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(time_diff)))
            self.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(data[2][0])+", "+str(data[3][0])+", "+str(data[4][0])+", "+str(data[5][0])))
            self.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(data[2][1])+", "+str(data[3][1])+", "+str(data[4][1])+", "+str(data[5][1])))
            self.tableWidget.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(str(data[2][2])+", "+str(data[3][2])+", "+str(data[4][2])+", "+str(data[5][2])))
            self.tableWidget.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(str(data[2][3])+", "+str(data[3][3])+", "+str(data[4][3])+", "+str(data[5][3])))
            self.tableWidget.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(str(data[2][4])+", "+str(data[3][4])+", "+str(data[4][4])+", "+str(data[5][4])))

    def start_click(self):
        self.ui = uic.loadUi("gaming.ui", self)
        self.setWindowTitle('Multiplication Challenge')
        self.game_count = 1
        self.correct = 0
        self.record = record()
        self.show()
        self.pushButton_2.clicked.connect(self.clicked_2)
        self.pushButton_3.clicked.connect(self.clicked_3)
        self.pushButton_4.clicked.connect(self.clicked_4)
        self.pushButton_5.clicked.connect(self.clicked_5)
        self.game()

    def game(self):
        self.game_initialization()
            
        #change game count
        print(self.game_count)
        self.label_5.setText("Q" + str(self.game_count)+ ":");
            
        x = randrange(10) + 1
        y = randrange(10) + 1
        correct_answer = x*y
        dummy_1 = correct_answer
        dummy_2 = correct_answer
        while dummy_1 == correct_answer:
            dummy_1 = randrange(100) + 1
        while dummy_2 == correct_answer:
            dummy_2 = randrange(100) + 1

        #button 2,3,4
        self.correct_position = randrange(3) + 2

        question = str(x) + " * " + str(y) + " = ?"
        self.label_6.setText(question);
        
        #append question/correct answer
        self.record.question.append(question)
        self.record.correct_answer.append(correct_answer)

        if self.correct_position == 2:
            self.pushButton_2.setText(str(correct_answer));
            self.pushButton_3.setText(str(dummy_1));
            self.pushButton_4.setText(str(dummy_2));
        if self.correct_position == 3:    
            self.pushButton_2.setText(str(dummy_1));
            self.pushButton_3.setText(str(correct_answer));
            self.pushButton_4.setText(str(dummy_2));
        if self.correct_position == 4:    
            self.pushButton_2.setText(str(dummy_2));
            self.pushButton_3.setText(str(dummy_1));
            self.pushButton_4.setText(str(correct_answer));
        
        self.show()

    def game_initialization(self):
        self.pushButton_5.hide()
        self.label_7.hide()
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_2.setStyleSheet(".QPushButton{\n"
        "background-color: #C4C4C4;\n"
        "font: 18pt \"Cooper Black\";\n"
        "border-radius: 15px;\n"
        "color: black; \n"
        "border: 2px solid #4CAF50;\n"
        "}\n"
        "\n"
        ".QPushButton:hover {\n"
        "  background-color: #4CAF50;\n"
        "  color: white;\n"
        "}")
        self.pushButton_3.setStyleSheet(".QPushButton{\n"
        "background-color: #C4C4C4;\n"
        "font: 18pt \"Cooper Black\";\n"
        "border-radius: 15px;\n"
        "color: black; \n"
        "border: 2px solid #4CAF50;\n"
        "}\n"
        "\n"
        ".QPushButton:hover {\n"
        "  background-color: #4CAF50;\n"
        "  color: white;\n"
        "}")
        self.pushButton_4.setStyleSheet(".QPushButton{\n"
        "background-color: #C4C4C4;\n"
        "font: 18pt \"Cooper Black\";\n"
        "border-radius: 15px;\n"
        "color: black; \n"
        "border: 2px solid #4CAF50;\n"
        "}\n"
        "\n"
        ".QPushButton:hover {\n"
        "  background-color: #4CAF50;\n"
        "  color: white;\n"
        "}")
    
    def clicked_2(self):
        self.record.answer_provided.append(self.pushButton_2.text())
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.show_correct_ans()
        if(self.correct_position == 2):
            self.record.isCorrect.append(True)
            self.correct = self.correct + 1
            self.label_7.setStyleSheet("background-color: lightgreen;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Well done! you got the right answer :)")
        else:
            self.record.isCorrect.append(False)
            self.pushButton_2.setStyleSheet(".QPushButton{\n"
            "background-color: red;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")
            self.label_7.setStyleSheet("background-color: IndianRed;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Failure is the mother of success!")
        self.label_7.show()
        self.pushButton_5.show()

    def clicked_3(self):
        self.record.answer_provided.append(self.pushButton_3.text())
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.show_correct_ans()
        if(self.correct_position == 3):
            self.record.isCorrect.append(True)
            self.correct = self.correct + 1
            self.label_7.setStyleSheet("background-color: lightgreen;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Well done! you got the right answer :)")
        else:
            self.record.isCorrect.append(False)
            self.pushButton_3.setStyleSheet(".QPushButton{\n"
            "background-color: red;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")
            self.label_7.setStyleSheet("background-color: IndianRed;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Failure is the mother of success!")
        self.label_7.show()
        self.pushButton_5.show()

    def clicked_4(self):
        self.record.answer_provided.append(self.pushButton_4.text())
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.show_correct_ans()
        if(self.correct_position == 4):
            self.record.isCorrect.append(True)
            self.correct = self.correct + 1
            self.label_7.setStyleSheet("background-color: lightgreen;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Well done! you got the right answer :)")
        else:
            self.record.isCorrect.append(False)
            self.pushButton_4.setStyleSheet(".QPushButton{\n"
            "background-color: red;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")
            self.label_7.setStyleSheet("background-color: IndianRed;\n"
            "font: 10pt \"Times New Roman\";\n")
            self.label_7.setText("Failure is the mother of success!")
        self.label_7.show()
        self.pushButton_5.show()

    def show_correct_ans(self):
        if self.correct_position == 2:
            self.pushButton_2.setStyleSheet(".QPushButton{\n"
            "background-color: green;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")
        if self.correct_position == 3:
            self.pushButton_3.setStyleSheet(".QPushButton{\n"
            "background-color: green;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")
        if self.correct_position == 4:
            self.pushButton_4.setStyleSheet(".QPushButton{\n"
            "background-color: green;\n"
            "font: 18pt \"Cooper Black\";\n"
            "border-radius: 15px;\n"
            "color: black; \n"
            "border: 2px solid #4CAF50;\n"
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "  background-color: #4CAF50;\n"
            "  color: white;\n"
            "}")

    def clicked_5(self):
        self.game_count = self.game_count + 1
        if self.game_count <= self.max_round:
            self.game()
        else:
            self.ui = uic.loadUi("summary.ui", self)
            self.setWindowTitle('Multiplication Challenge')
            self.label_7.setText(str(self.correct) + " / " + str(self.max_round))
            if self.correct <= math.ceil(self.max_round / 3) :
                self.label_5.setStyleSheet("background-color: IndianRed;\n"
                "font: 14pt \"Times New Roman\";\n")
                self.label_5.setText("Room for improvement!")
            elif self.correct <= 2 * math.ceil(self.max_round / 3) :
                self.label_5.setStyleSheet("background-color: lightgreen;\n"
                "font: 14pt \"Times New Roman\";\n")
                self.label_5.setText("Good!")
            else:
                self.label_5.setStyleSheet("background-color: green;\n"
                "font: 14pt \"Times New Roman\";\n")
                self.label_5.setText("Well done!")
            self.show()

            self.record.finish_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            with open("records.txt", "a") as myfile:
                myfile.write(self.record.get_output_string())
                myfile.write("\n")
            self.pushButton_6.clicked.connect(self.restart)

    def restart(self):
        self.ui = uic.loadUi("menu.ui", self)
        self.setWindowTitle('Multiplication Challenge')
        self.show()

        start_button = self.pushButton
        start_button.clicked.connect(self.start_click)
        self.pushButton_2.clicked.connect(self.performance)
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = menu_ui()

    sys.exit(app.exec_())