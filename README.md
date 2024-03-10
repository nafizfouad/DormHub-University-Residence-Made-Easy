# DormHub: University Residence Made Easy

Welcome to the README for DormHub: University Residence Made Easy! This document provides information on how to set up and launch the project locally also the project description, architecture and the workflow of how the project was developed along with a brief description of the team which developed this project.

## Team - Fullsoftware Fusion
We are team Fullsoftware Fusion from CSE, Jahangirnagar University. We are passionate about developing quality software products from scratch. We developed this project as a software quality assurance project of one of our academic courses.

### Team Members
1.`Md. Nafiz Fouad Sarker` \
2.`Afzal Hossain Babor` \
3.`Mundim Ahsan Uosmoy` \
4.`Omar Farouque` \
5.`Md. Shagor Hossain`

## Skills and Expertise
* ⚛ Django
* 📱 VS Code
* 💻 HTML, CSS, JS, Python, Bootstrap

Installing Our Django Project
-----------------------------
## Prerequisites

Before getting started, ensure you have the following installed on your machine:

- Python (3.x recommended)
- pip (Python package installer)
- virtualenv (recommended for isolating project dependencies)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/nafizfouad/DormHub-University-Residence-Made-Easy.git

2. Navigate to the project directory:

    ```bash

   cd Hall_Management

3. Create a virtual environment (optional but recommended):

    ```bash
     python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash

    .\venv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash

    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash

    pip install -r requirements.txt
    ```
6. Apply database migrations:

    ```bash

    python manage.py migrate
    ```

7. Create a superuser (for Django admin access):

   ```bash

   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash

   python manage.py runserver
   ```

# Project Description

## Overview

This is a web application that automates all the managerial function that occurs within a hall/dormitory of a university. Starting from assigning students to dormitories, alloting rooms to each student, swapping rooms as per students' request, keeping logs of all the personnel who enters and leaves a dormitory to deallocating a student when they leave the dormitory, all these events can be handled using this web application. This app offers a centralized platform for efficiently managing all aspects of university hall/dormitory operations. By leveraging technology to automate processes and streamline communication, the system enhances convenience, transparency, and accountability for students, staff, and administrators alike, ultimately contributing to an improved living experience within university halls.

## Features

### 1. Hall Creation 

Administrators can create and manage halls within the system, defining the capacity, amenities, and other relevant details.

### 2. Student Management

Hall staff can easily add students to the system, maintaining accurate records of residents and their relevant information.

### 3. Complaint Management

Students can submit complaints regarding facilities or services through the system, which hall staff can promptly address and resolve.

### 4. Service Requests

Students can request various services, such as maintenance or cleaning, through the system, allowing hall staff to efficiently manage and fulfill these requests.

### 5. Online Payment

The system facilitates online payment of monthly seat fees, providing students with a convenient and secure method to fulfill their financial obligations.

### 6. Room Swap Requests

Students can request room swaps within the system, specifying their preferences and reasons for the swap.

### 7. Processing Room Swap Requests

Hall staff can review and process room swap requests, considering factors such as availability, preferences, and eligibility.

### 8. Room Allocation

The system automates the allocation of rooms to students based on predefined criteria, optimizing occupancy and ensuring fair distribution.

### 9. Visitor Entry Logs

Hall staff can maintain detailed logs of visitor entries, recording information such as visitor identity, purpose of visit, and duration of stay for security and administrative purposes.

## Actors:

### 1. Admin

Manages the system configuration, user permissions, and overall administration, ensuring the smooth functioning of the hall management system.

### 2. Provost

Oversees the overall management of the hall, with access to administrative functionalities for monitoring and decision-making.

### 3. Student

Utilizes the system to manage accommodation-related tasks, such as submitting complaints, requesting services, paying fees, and applying for room swaps.

### 4. Staff

Responsible for day-to-day operations, including adding students, addressing complaints, processing service requests, and managing room allocations.

## Implementation

The DormHub: University Residence Made Easy Web App is implemented using the Django web framework, providing a scalable and maintainable solution. The app features a clean and intuitive interface, making it easy for all the actors of the system to navigate and use it.

## Wiki Pages

The github wiki pages of this project contains all the documentations on developing the project from scratch. Starting from system requirement specification to app documentation, the wiki pages gives a clear idea on how the project was developed.

Wiki Pages:<br>
[![Wiki Pages](https://github.com/JU-CSE-27/swe-wiki/blob/master/resources/check-it-out.svg)](https://github.com/JU-CSE-27/swe-wiki/wiki)
<br>
Coding Principles:<br>
[![Wiki Pages](https://github.com/JU-CSE-27/swe-wiki/blob/master/resources/check-it-out.svg)](https://github.com/nafizfouad/DormHub-University-Residence-Made-Easy/wiki/Coding-Principles)
<br>
Sphinx Documentation:<br>
[![Wiki Pages](https://github.com/JU-CSE-27/swe-wiki/blob/master/resources/check-it-out.svg)](https://github.com/nafizfouad/DormHub-University-Residence-Made-Easy/wiki/Sphinx%E2%80%90Documentation)
<br>
SRS:<br>
[![Wiki Pages](https://github.com/JU-CSE-27/swe-wiki/blob/master/resources/check-it-out.svg)](https://github.com/nafizfouad/DormHub-University-Residence-Made-Easy/wiki/Software-Requirements-Specification)
<br>

