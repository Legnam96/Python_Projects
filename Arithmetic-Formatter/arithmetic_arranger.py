def arithmetic_arranger(problems, show_anwers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_line = str()
  second_line = str()
  third_line = str()
  answers = str()
  phrase = str()
  spaces = "    "

  for problem in problems:
    operand1 = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    operand2 = problem.split(" ")[2]

    if len(operand1) >= 5 or len(operand2) >= 5:
      return "Error: Numbers cannot be more than four digits."
    if str(operator) == "/" or str(operator) == "*":
      return "Error: Operator must be '+' or '-'."
    try:
      int(operand1) is True
      int(operand2) is True
    except:
      return "Error: Numbers must only contain digits."

    sum = str()
    if operator == "+":
      sum = str(int(operand1) + int(operand2))
    elif operator == "-":
      sum = str(int(operand1) - int(operand2))

    length = max(len(operand1), len(operand2)) + 2
    top = str(operand1).rjust(length)
    bottom = operator + str(operand2).rjust(length - 1)
    lines = str()
    result = str(sum).rjust(length)
    for space in range(length):
      lines += "-"

    if problem != problems[-1]:
      first_line += top + spaces
      second_line += bottom + spaces
      third_line += lines + spaces
      answers += result + spaces
    else:
      first_line += top
      second_line += bottom
      third_line += lines
      answers += result

  if show_anwers:
    phrase = first_line + "\n" + second_line + "\n" + third_line + "\n" + answers
  else:
    phrase = first_line + "\n" + second_line + "\n" + third_line
  return phrase
