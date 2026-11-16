from flask import Flask, jsonify, request

app = Flask(__name__)


schedule_list = [
    {
        "id": 1,
        "subject": "Công nghệ Phần mềm",
        "room": "A2.201",
        "time": "07:30 - 09:30",
        "day": "Thứ 2",
    },
    {
        "id": 2,
        "subject": "Lập trình Web",
        "room": "B1.102",
        "time": "09:30 - 11:30",
        "day": "Thứ 4",
    },
]



@app.route("/api/schedule", methods=["GET"])
def get_schedule():
    return jsonify({"status": "success", "data": schedule_list})



@app.route("/api/schedule", methods=["POST"])
def add_schedule():
    new_item = request.json
    new_item["id"] = (
        len(schedule_list) + 1
    ) 
    schedule_list.append(new_item)
    return (
        jsonify(
            {
                "status": "success",
                "message": "Đã thêm lịch học thành công!",
                "data": new_item,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
