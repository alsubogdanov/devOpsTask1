from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = [
    {"city": "Tel Aviv", "population": 450000},
    {"city": "Haifa", "population": 280000},
    {"city": "Jerusalem", "population": 900000}
]

# ------------------ GET ------------------
# http://localhost:5000/get/city
@app.route('/get/<city>', methods=['GET'])
def get_data(city):
    # value = data_store.get(city)
    result = next((item for item in data_store if item["city"] == city), None)

    if result:
        return jsonify(result), 200
    else:
        print("city not found")
        return jsonify({"error": "City not found"}), 404

# http://localhost:5000/getall
@app.route('/getall', methods=['GET'])
def get_all():
    return jsonify(data_store), 200

# ------------------ POST ------------------
# http://localhost:5000/add
# {
#   "city": "Nagariya",
#   "population": "123123"
# }
@app.route('/add', methods=['POST'])
def add_data():
    json_data = request.get_json()
    city = json_data.get('city')
    population = json_data.get('population')

    if city and population:
        data_store.append({'city': city, 'population': population})
        print(data_store)
        return jsonify({"message": f"{city} added"}), 201

    return jsonify({"error": "Invalid data"}), 400

# ------------------ DELETE ------------------
# http://localhost:5000/delete/city
@app.route('/delete/<city>', methods=['DELETE'])
def delete_data(city):
    global data_store
    original_length = len(data_store)
    data_store = [item for item in data_store if item['city'].lower() != city.lower()]

    if len(data_store) < original_length:
        return jsonify({"message": f"{city} deleted"}), 200
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
