import json
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from rest_framework import status

class TicketTestCase(APITestCase):

	# for creating A Movie
	def movie_creation(self):
		movie_data = {"title": "testMovie", 
					"price": 400,
					"poster": "default.jpg"}

		movie_data2 = {"title": "testMovie2", 
					"price": 800,
					"poster": "another.jpg"}

		self.client.post("/api/movie/create", movie_data)
		self.client.post("/api/movie/create", movie_data2)


	# for creating a timing
	def timing_creation(self):
		timing_data = {"time": "04:00 AM"}

		timing_data2 = {"time": "08:00 PM"}

		timing_data3 = {"time": "06:00 PM"}

		timing_data4 = {"time": "10:00 PM"}


		self.client.post("/api/timing/create", timing_data)
		self.client.post("/api/timing/create", timing_data2)
		self.client.post("/api/timing/create", timing_data3)
		self.client.post("/api/timing/create", timing_data4)

	def test_ticket_creation(self):
		
		# we need to create a movie inorder to create a ticket
		self.movie_creation()

		# we need to create a show timing inorder to create a ticket
		self.timing_creation()

		# Booking the ticket
		data = {"username": "testcase", 
				"phone": 1234567809,
				"movie": 1,
				"timing": 1}

		data2 = {"username": "testcase", 
				"phone": 5698321407,
				"movie": 2,
				"timing": 2}


		response = self.client.post("/api/ticket/create", data)
		self.client.post("/api/ticket/create", data2)

		# checking if ticket was created
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)

		print("Tickets Created Successfully")

	
	def test_update_ticket(self):

		# we need a ticket inorder to update it
		self.test_ticket_creation()

		# Updating data
		new_data = {"username": "newtestcase", 
				"phone": 9876543201,
				"movie": 2,
				"timing": 3}

		response = self.client.put("/api/ticket/1/update", new_data)

		# checking if details were updated successfully
		self.assertEquals(response.status_code, status.HTTP_200_OK)

		print("Ticket Updated Successfully")

	def test_tickets_on_time(self):
		
		# we need ticket inorder to view them based on time
		self.test_ticket_creation()

		# timing id 
		slug = 1

		response = self.client.get(f"/api/ticket/time/{slug}")
		# checking if data is there
		self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

		print("Checked if tickets are returned on basis of timing")


	def test_delete_ticket(self):

		# we need tickets inorder to delete them
		self.test_ticket_creation()


		# ticket id
		slug = 1

		response = self.client.delete(f"/api/ticket/{slug}/delete")

		#checking if ticket was deleted successfully
		self.assertEquals(response.status_code, status.HTTP_200_OK)

		print("Ticket deleted Successfully")

	def test_user_details_on_ticket_id(self):

		# we need some tickets
		self.test_ticket_creation()

		# ticket id
		slug = 1

		response = self.client.get(f"/api/ticket/{slug}")
		print(response.items)

		# checking if data is there
		self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

		print("Checked user's details through ticked id")