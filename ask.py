import aqgFunction
import sys
import numpy as np

# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    inputTextPath = sys.argv[1]
    num_questions = int(sys.argv[2])

    readFile = open(inputTextPath, 'r+', encoding="utf8")
    inputText = readFile.read()
    questionList = aqg.aqgParse(inputText)
    ques = np.array(aqg.display(questionList))

    index = np.random.choice(len(ques), num_questions, replace=False)
    for i in ques[index]:
        print(i)
    return 0


# Call Main Function
if __name__ == "__main__":
    main()

