-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, drop tables if they already exist so we start fresh every time we seed
DROP TABLE IF EXISTS tech_terms;

CREATE TABLE tech_terms (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    concept_name VARCHAR(255),
    analogy TEXT,
    key_notes TEXT,
    deep_dive TEXT
);

-- Batch #1 Complete Deep Dive Seeding
INSERT INTO tech_terms (topic, concept_name, analogy, key_notes, deep_dive) VALUES 
(
 'Backend', 
 'API', 
 'A waiter in a restaurant taking your order to the kitchen and bringing back food.', 
 'Application Programming Interface. Connects separate code components or interfaces.',
 'An API (Application Programming Interface) acts as a formal contract between two software systems. In modern web development, this usually means a RESTful API communicating over HTTP. When talking to Lloyds, mention how frontend applications execute asynchronous JS "fetch" requests or Python "requests" to distinct endpoints (like /api/v1/users). The backend processes the request, communicates with the database, and serializes the raw database records into clean JSON payloads returned with appropriate HTTP status codes (like 200 OK or 404 Not Found).'
),
(
 'Database', 
 'Relational (SQL) vs. NoSQL', 
 'SQL is a neat Excel spreadsheet with locked rows. NoSQL is a folder of random mixed sticky notes.', 
 'SQL handles highly structured tables with relations (PostgreSQL). NoSQL handles loose unstructured document stores (MongoDB).',
 'Relational databases (SQL) rely on a strict, predefined schema where data is stored across tables with fixed columns, enforcing data integrity through primary and foreign key constraints. This is critical for ACID compliance (Atomicity, Consistency, Isolation, Durability)—which banking institutions like Lloyds absolute care about for financial transactions. Non-Relational databases (NoSQL), like document stores, save data as loose JSON-like structures. They lack rigid schemas, making them highly horizontally scalable and ideal for unstructured data, logging, or rapid prototyping where requirements shift constantly.'
),
(
 'Frontend', 
 'The DOM', 
 'The architectural blueprint framework of a house. JavaScript uses it to dynamically repaint walls or move furniture.', 
 'Document Object Model. The structural representation of HTML objects that browsers read and interact with.',
 'The DOM (Document Object Model) is an API created by the browser when a web page loads. It represents the raw HTML document as a logical tree structure where every node is an object representing a piece of the page. Frontend JavaScript interacts with this tree via the global "document" object to dynamically modify elements, update styling, or attach event listeners (like user clicks) without executing a full page refresh. In modern development frameworks, managing DOM performance is key, as frequent direct DOM manipulation can cause expensive browser repaints and reflows.'
),
(
 'DevOps', 
 'CI/CD Pipeline', 
 'An automated car assembly line that runs continuous safety checks and paints cars automatically before rolling them onto the lot.', 
 'Continuous Integration / Continuous Deployment. Automates code testing, building, and live server updates.',
 'CI/CD is a core DevOps practice focused on automating the software shipping lifecycle. Continuous Integration (CI) means that every time a developer pushes code to a shared repository (like GitHub), an automated server triggers an isolated environment to install dependencies, run linter checks, and execute the automated test suite (e.g., Pytest) to catch integration bugs early. Continuous Deployment (CD) builds on this: if all checks pass seamlessly on the main branch, the pipeline automatically packages the application and deploys it to staging or production infrastructure without human intervention.'
);