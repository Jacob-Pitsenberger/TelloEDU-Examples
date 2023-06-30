"""
Author: Jacob Pitsenberger
Program: flight_info.py
Version: 1.0
Project: TelloEDU Demos
Date: 6/30/2023
Purpose: This module demonstrates getting hardware and flight data from the telloEDU and displaying
		 the status data in video stream window and printing orientation data as output.
Future Enhancements: - Display data in Tkinter window.
					 - Write data to csv files and save them to sqlite database.
"""

import sys
import cv2
from djitellopy import tello


def get_orientation_data(drone):
	"""Print the orientation data from the TelloEDU in a readable string format.
	Velocities return in decimeters per second so converting to meters per second using conversion factor of 0.1"""
	pitch = 'Pitch: ' + str(drone.get_pitch()) + '°'
	roll = 'Roll: ' + str(drone.get_roll()) + '°'
	yaw = 'Yaw: ' + str(drone.get_yaw()) + '°'
	vgx = 'Speed X: ' + str(0.1 * drone.get_speed_x()) + 'm/s'
	vgy = 'Speed Y: ' + str(0.1 * drone.get_speed_y()) + 'm/s'
	vgz = 'Speed Z: ' + str(0.1 * drone.get_speed_z()) + 'm/s'
	agx = 'Acceleration X: ' + str(drone.get_acceleration_x()) + 'cm/s²'
	agy = 'Acceleration Y: ' + str(drone.get_acceleration_y()) + 'cm/s²'
	agz = 'Acceleration Z: ' + str(drone.get_acceleration_z()) + 'cm/s²'
	print(
		pitch + "\n" + roll + "\n" + yaw + "\n" + vgx + "\n" + vgy + "\n" + vgz + "\n" + agx + "\n" + agy + "\n" + agz)


def get_status_data(drone):
	"""Get the drones current status data and return it as variables."""
	activeMotorTime = drone.get_flight_time()
	battery = drone.get_battery()
	height = drone.get_height()
	tof = drone.get_distance_tof()  # 'cm'
	templ = drone.get_lowest_temperature()
	temph = drone.get_highest_temperature()
	avgTemp = drone.get_temperature()
	baramoter = drone.get_barometer()
	return activeMotorTime, battery, height, tof, templ, temph, avgTemp, baramoter


def main():
	# Connect to the drone and start receiving video
	drone = tello.Tello()
	drone.connect()
	drone.streamon()
	while True:
		# Get the most recent orientation data
		get_orientation_data(drone)

		# Get the most recent frame
		frame = drone.get_frame_read().frame

		# Get status data variables by calling function
		activeMotorTime, battery, height, tof, templ, temph, avgTemp, baramoter = get_status_data(drone)

		# List the status data in white by writing it to the upper left hand corner of the video frame.
		cv2.putText(frame, 'Active Motor Time: ' + str(activeMotorTime) + ' Seconds', (10, 20),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'Battery: ' + str(battery) + '%', (10, 45),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'Height: ' + str(height) + ' cm', (10, 70),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'tof: ' + str(tof) + ' cm', (10, 95),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'templ: ' + str(templ) + ' Celsius', (10, 120),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'temph: ' + str(temph) + ' Celsius', (10, 145),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'Avg temp: ' + str(avgTemp) + ' Celsius', (10, 170),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		cv2.putText(frame, 'Baramoter: ' + str(baramoter) + ' cm (abs height)', (10, 195),
					cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, 2)

		# Show the video stream with the status data written to it.
		cv2.imshow("Frame", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			print("Ending the Tello Object...")
			drone.end()
			sys.exit("Tello Object Deleted. Exiting the code with sys.exit()!")


if __name__ == "__main__":
	main()
