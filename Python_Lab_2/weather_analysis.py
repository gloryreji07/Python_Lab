from typing import List, Dict, Tuple

weather_data: List[Dict[str, any]] = [
    {"date": "2024-08-01", "max_temp": 29, "min_temp": 20, "humidity": 75},
    {"date": "2024-08-02", "max_temp": 31, "min_temp": 22, "humidity": 80},
    {"date": "2024-08-03", "max_temp": 33, "min_temp": 23, "humidity": 70},
    {"date": "2024-08-04", "max_temp": 32, "min_temp": 24, "humidity": 65},
    {"date": "2024-08-05", "max_temp": 30, "min_temp": 22, "humidity": 60},
    {"date": "2024-08-06", "max_temp": 28, "min_temp": 21, "humidity": 85},
    {"date": "2024-08-07", "max_temp": 29, "min_temp": 22, "humidity": 77},
    {"date": "2024-08-08", "max_temp": 30, "min_temp": 23, "humidity": 70},
    {"date": "2024-08-09", "max_temp": 31, "min_temp": 22, "humidity": 75},
    {"date": "2024-08-10", "max_temp": 29, "min_temp": 21, "humidity": 80},
   
]

def find_highest_lowest_temps(data: List[Dict[str, any]]) -> Tuple[int, int]:
    """Find the highest and lowest temperatures recorded during the period."""
    max_temp = max(day["max_temp"] for day in data)
    min_temp = min(day["min_temp"] for day in data)
    return max_temp, min_temp

def count_days_above_30(data: List[Dict[str, any]]) -> int:
    """Determine the number of days with temperatures above 30°C."""
    count = sum(1 for day in data if day["max_temp"] > 30)
    return count

def average_humidity(data: List[Dict[str, any]]) -> float:
    """Compute the average humidity over the specified period."""
    total_humidity = sum(day["humidity"] for day in data)
    average = total_humidity / len(data)
    return average

def demonstrate_weather_analysis():
    highest_temp, lowest_temp = find_highest_lowest_temps(weather_data)
    print(f"Highest Temperature: {highest_temp}°C")
    print(f"Lowest Temperature: {lowest_temp}°C")
    
    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of Days with Temperature Above 30°C: {days_above_30}")
    
    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity:.2f}%")

if __name__ == "__main__":
    demonstrate_weather_analysis()
