from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

# Load subject data
def load_subject_data(subject):
    try:
        with open(f'data/{subject}_topics.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        if subject == 'chemistry':
            return {
                "title": "เคมี",
                "sections": [
                    {
                        "id": "properties",
                        "title": "สมบัติของธาตุและสารประกอบ",
                        "topics": [
                            {"id": "atomic", "title": "อะตอมและสมบัติของธาตุ", "animation_path": "/animations/chemistry/atomic_structure"},
                            {"id": "bond", "title": "พันธะเคมี", "animation_path": "/animations/chemistry/chemical_bonds"},
                            {"id": "gas", "title": "แก๊ส", "animation_path": "/animations/chemistry/gases"},
                            {"id": "organic", "title": "เคมีอินทรีย์", "animation_path": "/animations/chemistry/organic_chemistry"},
                            {"id": "polymer", "title": "พอลิเมอร์", "animation_path": "/animations/chemistry/polymers"}
                        ],
                        "questions": "15 - 17 ข้อ"
                    },
                    {
                        "id": "equations",
                        "title": "สมการเคมีและการเปลี่ยนแปลงทางเคมี",
                        "topics": [
                            {"id": "stoichiometry", "title": "ปริมาณสัมพันธ์", "animation_path": "/animations/chemistry/stoichiometry"},
                            {"id": "rate", "title": "อัตราการเกิดปฏิกิริยาเคมี", "animation_path": "/animations/chemistry/reaction_rates"},
                            {"id": "equilibrium", "title": "สมดุลเคมี", "animation_path": "/animations/chemistry/chemical_equilibrium"},
                            {"id": "acidbase", "title": "กรด–เบส", "animation_path": "/animations/chemistry/acid_base"},
                            {"id": "electrochemistry", "title": "เคมีไฟฟ้า", "animation_path": "/animations/chemistry/electrochemistry"}
                        ],
                        "questions": "15 - 17 ข้อ"
                    },
                    {
                        "id": "lab",
                        "title": "ทักษะในปฏิบัติการเคมีและการคำนวณปริมาณของสาร",
                        "topics": [
                            {"id": "safety", "title": "ความปลอดภัยและทักษะในปฏิบัติการเคมี", "animation_path": "/animations/chemistry/lab_safety"},
                            {"id": "mole", "title": "โมล", "animation_path": "/animations/chemistry/mole_concept"},
                            {"id": "solution", "title": "สารละลาย", "animation_path": "/animations/chemistry/solutions"}
                        ],
                        "questions": "2 - 4 ข้อ"
                    }
                ],
                "exam_info": {
                    "type": "ปรนัย (5 ตัวเลือก) / ระบายคำตอบที่เป็นตัวเลข",
                    "duration": "90 นาที",
                    "year": "65"
                },
                "theme_color": "#2ecc71",
                "theme_dark": "#27ae60",
                "icon": "flask"
            }
        elif subject == 'mathematics':
            return {
                "title": "คณิตศาสตร์",
                "sections": [
                    {
                        "id": "algebra",
                        "title": "สาระจำนวนและพีชคณิต",
                        "topics": [
                            {"id": "sets", "title": "เซต", "animation_path": "/animations/mathematics/sets"},
                            {"id": "logic", "title": "ตรรกศาสตร์", "animation_path": "/animations/mathematics/logic"},
                            {"id": "realnumbers", "title": "จำนวนจริงและพหุนาม", "animation_path": "/animations/mathematics/real_numbers"},
                            {"id": "functions", "title": "ฟังก์ชัน", "animation_path": "/animations/mathematics/functions"},
                            {"id": "exponential", "title": "ฟังก์ชันเอกซ์โพเนนเชียลและฟังก์ชันลอการิทึม", "animation_path": "/animations/mathematics/exponential_functions"},
                            {"id": "trigonometry", "title": "ฟังก์ชันตรีโกณมิติ", "animation_path": "/animations/mathematics/trigonometric_functions"},
                            {"id": "complex", "title": "จํานวนเชิงซ้อน", "animation_path": "/animations/mathematics/complex_numbers"},
                            {"id": "matrices", "title": "เมทริกซ์", "animation_path": "/animations/mathematics/matrices"},
                            {"id": "sequences", "title": "ลําดับและอนุกรม", "animation_path": "/animations/mathematics/sequences_series"}
                        ],
                        "questions": "15 - 17 ข้อ"
                    },
                    {
                        "id": "geometry",
                        "title": "สาระการวัดและเรขาคณิต",
                        "topics": [
                            {"id": "analytical", "title": "เรขาคณิตวิเคราะห์", "animation_path": "/animations/mathematics/analytical_geometry"},
                            {"id": "vectors", "title": "เวกเตอร์ในสามมิติ", "animation_path": "/animations/mathematics/3d_vectors"}
                        ],
                        "questions": "3 - 5 ข้อ"
                    },
                    {
                        "id": "statistics",
                        "title": "สาระสถิติและความน่าจะเป็น",
                        "topics": [
                            {"id": "stats", "title": "สถิติ", "animation_path": "/animations/mathematics/statistics"},
                            {"id": "probability_dist", "title": "การแจกแจงความน่าจะเป็นเบื้องต้น", "animation_path": "/animations/mathematics/probability_distributions"},
                            {"id": "counting", "title": "หลักการนับเบื้องต้น", "animation_path": "/animations/mathematics/counting_principles"},
                            {"id": "probability", "title": "ความน่าจะเป็น", "animation_path": "/animations/mathematics/probability"}
                        ],
                        "questions": "6 - 8 ข้อ"
                    },
                    {
                        "id": "calculus",
                        "title": "สาระแคลคูลัส",
                        "topics": [
                            {"id": "intro_calculus", "title": "แคลคูลัสเบื้องต้น", "animation_path": "/animations/mathematics/intro_calculus"}
                        ],
                        "questions": "2 - 4 ข้อ"
                    }
                ],
                "exam_info": {
                    "type": "ปรนัย 5 ตัวเลือก / ระบายคำตอบที่เป็นตัวเลข",
                    "duration": "90 นาที",
                    "year": "61"
                },
                "theme_color": "#e74c3c",
                "theme_dark": "#c0392b",
                "icon": "square-root-variable"
            }
        elif subject == 'physics':
            return {
                "title": "ฟิสิกส์",
                "sections": [
                    {
                        "id": "mechanics",
                        "title": "กลศาสตร์",
                        "topics": [
                            {"id": "nature", "title": "ธรรมชาติและพัฒนาการทางฟิสิกส์", "animation_path": "/animations/physics/nature_of_physics"},
                            {"id": "linear_motion", "title": "การเคลื่อนที่แนวตรง", "animation_path": "/animations/physics/linear_motion"},
                            {"id": "force", "title": "แรงและกฎการเคลื่อนที่", "animation_path": "/animations/physics/forces_laws"},
                            {"id": "equilibrium", "title": "สมดุลกลของวัตถุ", "animation_path": "/animations/physics/mechanical_equilibrium"},
                            {"id": "work_energy", "title": "งานและกฎการอนุรักษ์พลังงานกล", "animation_path": "/animations/physics/work_energy"},
                            {"id": "momentum", "title": "โมเมนตัมและการชน", "animation_path": "/animations/physics/momentum_collision"},
                            {"id": "curved_motion", "title": "การเคลื่อนที่แนวโค้ง", "animation_path": "/animations/physics/curved_motion"},
                            {"id": "shm", "title": "การเคลื่อนที่แบบฮาร์มอนิกส์อย่างง่าย", "animation_path": "/animations/physics/shm"}
                        ],
                        "questions": "9 - 10 ข้อ"
                    },
                    {
                        "id": "waves",
                        "title": "คลื่น",
                        "topics": [
                            {"id": "waves_basics", "title": "ธรรมชาติของคลื่น", "animation_path": "/animations/physics/waves_basics"},
                            {"id": "sound", "title": "เสียง", "animation_path": "/animations/physics/sound"},
                            {"id": "mechanical_waves", "title": "คลื่นกล", "animation_path": "/animations/physics/mechanical_waves"},
                            {"id": "light", "title": "แสง", "animation_path": "/animations/physics/light"}
                        ],
                        "questions": "7 - 8 ข้อ"
                    },
                    {
                        "id": "electricity",
                        "title": "ไฟฟ้า แม่เหล็ก",
                        "topics": [
                            {"id": "charge", "title": "ไฟฟ้าสถิต", "animation_path": "/animations/physics/electric_charge"},
                            {"id": "circuit", "title": "ไฟฟ้ากระแส", "animation_path": "/animations/physics/electric_circuit"},
                            {"id": "magnetic", "title": "แม่เหล็กไฟฟ้า", "animation_path": "/animations/physics/electromagnetism"}
                        ],
                        "questions": "7 - 8 ข้อ"
                    },
                    {
                        "id": "thermodynamics",
                        "title": "ความร้อนและเทอร์โมไดนามิกส์",
                        "topics": [
                            {"id": "heat", "title": "ความร้อน", "animation_path": "/animations/physics/heat"},
                            {"id": "thermo", "title": "กฎของเทอร์โมไดนามิกส์", "animation_path": "/animations/physics/thermodynamics"}
                        ],
                        "questions": "5 - 6 ข้อ"
                    },
                    {
                        "id": "modern",
                        "title": "ฟิสิกส์ยุคใหม่",
                        "topics": [
                            {"id": "atomic", "title": "ฟิสิกส์อะตอม", "animation_path": "/animations/physics/atomic_physics"},
                            {"id": "nuclear", "title": "ฟิสิกส์นิวเคลียร์", "animation_path": "/animations/physics/nuclear_physics"},
                            {"id": "relativity", "title": "ทฤษฎีสัมพัทธภาพพิเศษ", "animation_path": "/animations/physics/special_relativity"}
                        ],
                        "questions": "2 - 3 ข้อ"
                    }
                ],
                "exam_info": {
                    "type": "ปรนัย 5 ตัวเลือก / ระบายคำตอบที่เป็นตัวเลข",
                    "duration": "90 นาที",
                    "year": "64"
                },
                "theme_color": "#3498db",
                "theme_dark": "#2980b9",
                "icon": "atom"
            }
        else:
            return {}

# Routes
@app.route('/')
def index():
    # Just render the main page with links to all subjects
    return render_template('index.html')

@app.route('/subject/<subject>')
def subject(subject):
    # Load subject data
    subject_data = load_subject_data(subject)
    return render_template('subject.html', subject=subject, subject_data=subject_data)

@app.route('/topic/<subject>/<section_id>/<topic_id>')
def topic(subject, section_id, topic_id):
    # Load subject data
    subject_data = load_subject_data(subject)
    
    # Find the section
    section = next((s for s in subject_data['sections'] if s['id'] == section_id), None)
    
    if not section:
        return redirect(url_for('subject', subject=subject))
    
    # Find the topic
    topic = next((t for t in section['topics'] if t['id'] == topic_id), None)
    
    if not topic:
        return redirect(url_for('subject', subject=subject))
    
    return render_template('topic.html', 
                           subject=subject,
                           subject_data=subject_data, 
                           section=section, 
                           topic=topic)

@app.route('/animation/<path:animation_path>')
def animation(animation_path):
    # Render the animation template with the animation path
    return render_template('animation.html', animation_path=animation_path)

@app.route('/practice/<subject>')
def practice(subject):
    # Load subject data
    subject_data = load_subject_data(subject)
    return render_template('practice.html', subject=subject, subject_data=subject_data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)
