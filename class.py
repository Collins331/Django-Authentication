# classes

class Email:
  # __ means private
  __read = False

  def __init__(self, subject, body):
    self.subject = subject
    self.body = body

  def mark_as_read(self):
    self.__read = True

  def is_read(self):
    return self.__read

  def is_spam(self):
    return "you won 1 million" in self.subject

e = Email("Check this out", "There are a bunch of free online course here: https://course.online")
print(e.is_spam()) # False
print(e.mark_as_read())
print(e.is_read()) # True