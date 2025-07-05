t=int(input())
for _ in range(t):
  g=int(input())
  student_ids=[int(input()) for _ in range(g)]
  m=1
  while True:
    reminders=[sn%m for sn in student_ids]
    if len(set(reminders))==len(student_ids): print(m); break
    m+=1