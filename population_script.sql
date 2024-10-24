-- Insert job categories
INSERT INTO job_jobcategory (name) VALUES ('Software Engineering');
INSERT INTO job_jobcategory (name) VALUES ('Data Science');
INSERT INTO job_jobcategory (name) VALUES ('Product Management');
INSERT INTO job_jobcategory (name) VALUES ('IT & Systems');
INSERT INTO job_jobcategory (name) VALUES ('Marketing');
INSERT INTO job_jobcategory (name) VALUES ('Engineering');
INSERT INTO job_jobcategory (name) VALUES ('Sales');
INSERT INTO job_jobcategory (name) VALUES ('Human Resources');
INSERT INTO job_jobcategory (name) VALUES ('Finance');
INSERT INTO job_jobcategory (name) VALUES ('Operations');
INSERT INTO job_jobcategory (name) VALUES ('Customer Service');
INSERT INTO job_jobcategory (name) VALUES ('Design');
INSERT INTO job_jobcategory (name) VALUES ('Legal');
INSERT INTO job_jobcategory (name) VALUES ('Research & Development');
INSERT INTO job_jobcategory (name) VALUES ('Administration');
INSERT INTO job_jobcategory (name) VALUES ('Business Development');
INSERT INTO job_jobcategory (name) VALUES ('Quality Assurance');
INSERT INTO job_jobcategory (name) VALUES ('Education');
INSERT INTO job_jobcategory (name) VALUES ('Healthcare');
INSERT INTO job_jobcategory (name) VALUES ('Public Relations');

-- Insert company information
INSERT INTO company_company (name, description, address, logo, cover_image, user_id) VALUES
('Facebook', '<p>Facebook, a leading social media platform, connects billions of users globally, allowing them to share ideas, thoughts, and personal moments. Founded in 2004 by Mark Zuckerberg and his college roommates, it has evolved from a simple network for Harvard students to a vast ecosystem supporting various social applications and business tools.</p>', '1 Hacker Way, Menlo Park, CA 94025', 'company_logos/facebook_logo_gLWfEIs.png', 'company_covers/facebook_cover_YftqfKp.jpg', 1),
('Google', '<p>Tech leader and search engine powerhouse, Google has revolutionized information access and technology through continuous innovation. Google''s services include search engine technology, cloud computing, software, and hardware, making it one of the most influential companies in the tech industry.</p>', '1600 Amphitheatre Parkway, Mountain View, CA 94043', 'company_logos/google_logo_B0Dboci.png', 'company_covers/google_cover_t8ho9C9.jpg', 1),
('Tesla', '<p>Tesla is at the forefront of the electric vehicle and clean energy revolution. Founded by Elon Musk, Tesla produces electric cars, battery energy storage from home to grid scale, solar panels and solar roof tiles, and other products related to sustainable energy. Their commitment to innovation and sustainability has made them a major player in both the automotive and energy industries.</p>', '3500 Deer Creek Road, Palo Alto, CA 94304', 'company_logos/tesla_logo_qt9kSm3.png', 'company_covers/tesla_cover_NKdjOqB.jpg', 2),
('McDonald''s', '<p>McDonald''s is a global leader in the fast-food industry, known for its hamburgers, chicken, french fries, breakfast items, and soft drinks. Beyond its menu, McDonald''s is also noted for its speedy service, family-friendly dining experience, and global presence, making it one of the most recognizable brands worldwide. Its commitment to consistency and customer satisfaction has cemented its status as a cultural and commercial icon.</p>', '110 N Carpenter St, Chicago, IL 60607', 'company_logos/mcdonalds_logo_XHJV4Q9.png', 'company_covers/mcdonalds_cover_WhMfqOC.jpg', 2),
('Advania', '<p>Advania is a comprehensive IT service provider and consultancy firm with a strong presence across Northern Europe. Known for its extensive range of solutions, Advania specializes in cloud services, managed IT services, cybersecurity, and digital transformation. The company caters to various industries, offering tailored solutions to enhance business efficiency and innovation. With a commitment to customer-centric approaches, Advania combines cutting-edge technology with expert consultancy to help organizations achieve their strategic goals.</p>', 'Guðrúnartún 10', 'company_logos/advania_sweden_logo_s1Gjlt5.jpg', 'company_covers/Advania-Iceland-HQ-1024x683_VAwtWWz.jpg', 1);

-- Insert job information
INSERT INTO job_job (title, description, category_id, employment_type, location, start_date, due_date, created_at, company_id)
VALUES
('Software Engineer', '<p>Develop scalable web applications focusing on high availability, low latency and scalability in a distributed environment. Collaborate with cross-functional teams to define, design, and ship new features. Utilize various programming languages and tools to drive innovations and solutions.</p>', 1, 'FT', '1 Hacker Way, Menlo Park, CA 94025', '2024-07-01', '2024-06-01', '2024-05-16 19:26:53.550677 +00:00', 1),
('Data Scientist', '<p>Analyze large datasets using statistical techniques to derive business insights and develop predictive models. Implement data-driven solutions to solve complex business challenges. Present findings to stakeholders and provide recommendations based on data analysis.</p>', 2, 'PT', '1600 Amphitheatre Parkway, Mountain View, CA 94043', '2024-08-15', '2024-08-10', '2024-05-16 19:29:01.093182 +00:00', 2),
('Product Manager', '<p>Lead product development from ideation to launch, overseeing the design, development, and marketing teams. Define product vision and strategy, analyze market trends, and gather product requirements. Ensure products align with company goals and customer needs.</p>', 3, 'FT', '110 N Carpenter St, Chicago, IL 60607', '2024-06-20', '2024-06-11', '2024-05-16 19:31:08.240815 +00:00', 4),
('Systems Analyst', '<p>Optimize company IT infrastructure by assessing system performance and functionality. Identify issues and propose improvements to enhance efficiency and reduce costs. Collaborate with IT departments to implement systems upgrades and maintain security protocols.</p>', 4, 'FT', '1 Hacker Way, Menlo Park, CA 94025', '2024-09-14', '2024-08-21', '2024-05-16 19:32:32.292621 +00:00', 1);

-- Insert user contact information
INSERT INTO user_contactinformation (full_name, birthdate, phone_number, street_name, house_number, city, postal_code, country, from_profile, profile_id)
VALUES ('Davíð T. Óttarsson', '2003-06-26', '+354 695 4711', 'Lindasmári', '10', 'Kópavogur', '200', 'IS', True, 1);

-- Insert user references
INSERT INTO user_reference (name, role, email, phone_number, can_be_contacted, from_profile, profile_id)
VALUES
('Óttar Pálsson', 'CEO at Better Gardens', 'ottar@bettergardens.is', '+354 791 8332', True, True, 1),
('Ásgeir Orri', 'Shift manager at Jysk', 'asgeirorri@jysk.is', '+354 691 9272', False, True, 1);

-- Insert user experience
INSERT INTO user_experience (role, company_name, start_date, end_date, from_profile, profile_id)
VALUES
('Warehouse Assistant', 'Jysk', '2022-05-26', '2024-05-26', True, 1),
('Gardener', 'Better Gardens', '2021-06-26', '2022-03-26', True, 1);