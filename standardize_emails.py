from password import email_address, correspondence


def clean_email(filename, sender, receiver):
  new_file = open('texts/clean' + filename, 'w+')
  flag = False
  with open('texts/'+filename) as text:
    content = text.readlines()
    for line in content:
      line = line.lower()
      line = line.translate(None, ')(:]["?!$~')
      if sender[0] + ' ' + sender[1] in line:
        pass
      elif '>' in line or len(line)<3:
	pass
      elif sender[1] + ', ' + sender[0] in line or sender[0] + ' ' + sender[1] in line:

        print "in standardixe**** " + line
        pass
      elif receiver[1] + ', ' + receiver[0] in line or receiver[0] + ' ' + receiver[1] in line:
        pass
      elif '|' in line:
	pass
      elif email_address in line or correspondence in line or 'http' in line:
        pass
      elif 'chris' in line:
        flag = False
      elif 'i think it was last night  i was reading something' in line:
        flag = True
        pass
      elif flag == True:
        pass
      else:
        line = line.translate(None, '.,')
        new_file.write(line)
    new_file.close()

