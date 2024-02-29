# Facial Recognition App on AWS
![Facial Rekognition](https://github.com/agilscripts/AWS-Facial-Recognition-App/assets/143922871/f0bc7e7c-9ddf-4a80-9f27-705cbbce7ee1)


## Overview
This project is an end-to-end implementation of a Facial Recognition App on AWS, leveraging key services such as Amazon Rekognition, AWS Lambda, DynamoDB, API Gateway, and S3. The application is designed for employee authentication with a primary focus on security. It utilizes two separate S3 buckets – one for employee photos and another for visitor photos. The system not only verifies employee identities but also has the potential for future integration as a clock-in device, maintaining a log of employee entry times along with their names and employee IDs in DynamoDB.

## Features
### Amazon Rekognition:
Achieves highly accurate facial analysis for precise authentication.

### AWS Lambda:
Implements serverless architecture for scalability and cost-effectiveness.

### DynamoDB:
Manages identity data efficiently in real-time, storing employee information like name, employee ID, and entry times.

### API Gateway: 
Provides a secure communication interface for the app.

### S3 Buckets:
Maintains two separate buckets for employee and visitor photos.

## Usage
### Setup AWS Services:
Configure Amazon Rekognition, AWS Lambda, DynamoDB, and API Gateway through the AWS Management Console.

### Upload Photos:
Add employee photos to the designated S3 bucket for employees.
Upload visitor photos to the specified S3 bucket for visitors.

### Integration:
Integrate the app with your existing security systems or use it as a standalone authentication solution.

### Employee Verification:
Utilize the app for secure and precise employee authentication.

### Clock-In Integration (Future Feature):
Explore the option to use the app as a clock-in device, keeping track of employee entry times and maintaining records in DynamoDB.

## Future Enhancements
### Clock-In Feature:
Expand the application to function as a comprehensive clock-in device, recording employee entry times.

### User Interface:
Develop a user-friendly interface for easier interaction.
