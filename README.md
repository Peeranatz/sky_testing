วิธีรัน Test Cases และตรวจสอบ Coverage

การรัน Test Cases
รัน test cases แบบ verbose (แสดงผลลัพธ์แบบละเอียด):

python -m unittest -v {filename}

ตัวอย่าง

python -m unittest -v funnyString.py

การตรวจสอบ Coverage

รัน test cases พร้อมตรวจสอบ coverage:

coverage run -m unittest {filename}

ตัวอย่าง

coverage run -m unittest funnyString.py

สร้างรายงาน Coverage

สร้างรายงาน coverage แบบ text:

coverage report -m

สร้างรายงาน coverage แบบ HTML (Optional):

coverage html

จากนั้นเปิดไฟล์ htmlcov/index.html ในเบราว์เซอร์เพื่อดูรายงาน coverage แบบกราฟิก