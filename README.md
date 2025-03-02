# sky_testing
วิธีรัน Test Cases และตรวจสอบ Coverage

การรัน Test Cases
รัน test cases แบบ verbose (แสดงผลลัพธ์แบบละเอียด):
python -m unittest -v {filename}
ex python -m unittest -v funnyString.py

การตรวจสอบ Coverage
รัน test cases พร้อมตรวจสอบ coverage:

coverage run -m unittest {filename}
ex coverage run -m unittest funnyString.py

สร้างรายงาน coverage แบบ text:

coverage report -m
(Optional) สร้างรายงาน coverage แบบ HTML:

coverage html
เปิดไฟล์ htmlcov/index.html ในเบราว์เซอร์เพื่อดูรายงาน coverage แบบกราฟิก

