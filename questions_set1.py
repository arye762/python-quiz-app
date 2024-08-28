# General Security Concepts
questions_set1 = [
    {
        "question": "A company is developing a business continuity strategy and needs to determine how many staff members would be required to sustain the business in the case of a disruption. Which of the following best describes this step?",
        "options": [
            "Capacity planning",
            "Redundancy",
            "Geographic dispersion",
            "Tabletop exercise"
        ],
        "correct_answer": 1,
        "description": "Capacity planning involves determining the resources required to sustain business operations during disruptions."
    },
    {
        "question": "A company requires hard drives to be securely wiped before sending decommissioned systems to recycling. Which of the following best describes this policy?",
        "options": [
            "Enumeration",
            "Sanitization",
            "Destruction",
            "Inventory"
        ],
        "correct_answer": 2,
        "description": "Sanitization refers to securely wiping data from storage devices to ensure that it cannot be recovered, especially before disposing or repurposing the devices."
    },
    {
        "question": "A U.S.-based cloud-hosting provider wants to expand its data centers to new international locations. Which of the following should the hosting provider consider first?",
        "options": [
            "Local data protection regulations",
            "Risks from hackers residing in other countries",
            "Impacts to existing contractual obligations",
            "Time zone differences in log correlation"
        ],
        "correct_answer": 1,
        "description": "Local data protection regulations are crucial when expanding to international locations, as they govern how data must be handled and protected."
    },
    {
        "question": "Which of the following is the most likely outcome if a large bank fails an internal PCI DSS compliance assessment?",
        "options": [
            "Fines",
            "Audit findings",
            "Sanctions",
            "Reputation damage"
        ],
        "correct_answer": 1,
        "description": "Failure to comply with PCI DSS can lead to significant fines and penalties, especially for large financial institutions."
    },
    {
        "question": "Which of the following must be considered when designing a high-availability network? (Choose two).",
        "options": [
            "Ease of recovery",
            "Ability to patch",
            "Physical isolation",
            "Responsiveness",
            "Attack surface",
            "Extensible authentication"
        ],
        "correct_answer": [1, 4],
        "description": "High-availability networks require careful consideration of factors like ease of recovery and responsiveness to ensure minimal downtime."
    },

# Threats, Vulnerabilities, and Mitigation

    {
        "question": "Which of the following threat actors is the most likely to be hired by a foreign government to attack critical systems located in other countries?",
        "options": [
            "Hacktivist",
            "Whistleblower",
            "Organized crime",
            "Unskilled attacker"
        ],
        "correct_answer": 3,
        "description": "Organized crime groups are often highly skilled and have the resources to conduct sophisticated cyber-attacks, sometimes in collaboration with foreign governments."
    },
    {
        "question": "Which of the following is used to add extra complexity before using a one-way data transformation algorithm?",
        "options": [
            "Key stretching",
            "Data masking",
            "Steganography",
            "Salting"
        ],
        "correct_answer": 4,
        "description": "Salting is the process of adding extra complexity before applying a one-way data transformation algorithm to protect against brute-force attacks."
    },
    {
        "question": "An employee clicked a link in an email from a payment website that asked the employee to update contact information. The employee entered the log-in information but received a 'page not found' error message. Which of the following types of social engineering attacks occurred?",
        "options": [
            "Brand impersonation",
            "Pretexting",
            "Typosquatting",
            "Phishing"
        ],
        "correct_answer": 4,
        "description": "Phishing is a type of social engineering attack where an attacker sends fraudulent communications that appear to come from a reputable source, usually through email."
    },
    {
        "question": "Which of the following scenarios describes a possible business email compromise attack?",
        "options": [
            "An employee receives a gift card request in an email that has an executive’s name in the display field of the email.",
            "Employees who open an email attachment receive messages demanding payment in order to access files.",
            "A service desk employee receives an email from the HR director asking for log-in credentials to a cloud administrator account.",
            "An employee receives an email with a link to a phishing site that is designed to look like the company’s email portal."
        ],
        "correct_answer": 1,
        "description": "A Business Email Compromise (BEC) attack involves using a spoofed or compromised email account to trick employees into transferring money or revealing confidential information."
    },
    {
        "question": "A security analyst is reviewing logs that indicate multiple failed login attempts across several user accounts from different IP addresses. Which of the following attacks is most likely occurring?",
        "options": [
            "Password spraying",
            "Account forgery",
            "Pass-the-hash",
            "Brute-force"
        ],
        "correct_answer": 1,
        "description": "Password spraying is the attack where an attacker tries a small set of commonly used passwords across many accounts."
    },
    {
        "question": "A security team is reviewing the findings in a report that was delivered after a third party performed a penetration test. One of the findings indicated that a web application form field is vulnerable to cross-site scripting. Which of the following application security techniques should the security analyst recommend the developer implement to prevent this vulnerability?",
        "options": [
            "Secure cookies",
            "Version control",
            "Input validation",
            "Code signing"
        ],
        "correct_answer": 3,
        "description": "Input validation ensures that user inputs are properly sanitized before being processed by the application, helping prevent cross-site scripting (XSS) attacks."
    },
    {
        "question": "Which of the following vulnerabilities is associated with installing software outside of a manufacturer’s approved software repository?",
        "options": [
            "Jailbreaking",
            "Memory injection",
            "Resource reuse",
            "Side loading"
        ],
        "correct_answer": 4,
        "description": "Side loading is the vulnerability associated with installing software outside of a manufacturer’s approved software repository."
    },
    {
        "question": "Which of the following is a hardware-specific vulnerability?",
        "options": [
            "Firmware version",
            "Buffer overflow",
            "SQL injection",
            "Cross-site scripting"
        ],
        "correct_answer": 1,
        "description": "Firmware vulnerabilities are specific to the hardware on which the firmware is running."
    },
    {
        "question": "A company purchased cyber insurance to address items listed on the risk register. Which of the following strategies does this represent?",
        "options": [
            "Accept",
            "Transfer",
            "Mitigate",
            "Avoid"
        ],
        "correct_answer": 2,
        "description": "Purchasing cyber insurance represents the risk transfer strategy."
    },
    {
        "question": "Which of the following describes the reason root cause analysis should be conducted as part of incident response?",
        "options": [
            "To gather IoCs for the investigation",
            "To discover which systems have been affected",
            "To eradicate any trace of malware on the network",
            "To prevent future incidents of the same nature"
        ],
        "correct_answer": 4,
        "description": "Conducting a root cause analysis helps identify the underlying issues to prevent similar incidents in the future."
    },

# Security Architecture

    {
        "question": "A company prevented direct access from the database administrators’ workstations to the network segment that contains database servers. Which of the following should a database administrator use to access the database servers?",
        "options": [
            "Jump server",
            "RADIUS",
            "HSM",
            "Load balancer"
        ],
        "correct_answer": 1,
        "description": "A jump server is a secure system used to manage devices in a separate security zone."
    },
    {
        "question": "Which of the following methods is used to create an added layer of security by preventing unauthorized access to internal company resources?",
        "options": [
            "RDP server",
            "Jump server",
            "Proxy server",
            "Hypervisor"
        ],
        "correct_answer": 2,
        "description": "A Jump server creates an added layer of security by preventing unauthorized access to internal company resources."
    },
    {
        "question": "A data administrator is configuring authentication for a SaaS application and would like to reduce the number of credentials employees need to maintain. The company prefers to use domain credentials to access new SaaS applications. Which of the following methods would allow this functionality?",
        "options": [
            "SSO",
            "LEAP",
            "MFA",
            "PEAP"
        ],
        "correct_answer": 1,
        "description": "Single Sign-On (SSO) allows employees to use domain credentials to access SaaS applications, reducing the number of credentials they need to maintain."
    },
    {
        "question": "Which of the following scenarios best describes a Zero Trust principle in action?",
        "options": [
            "Using secured zones within the data plane to minimize access",
            "Implementing a bastion host for administrative access",
            "Using MFA for all network logins",
            "Ensuring all devices have antivirus software installed"
        ],
        "correct_answer": 1,
        "description": "Zero Trust principles include using secured zones within the data plane to minimize access and protect critical resources."
    },
    {
        "question": "An organization’s internet-facing website was compromised when an attacker exploited a buffer overflow. Which of the following should the organization deploy to best protect against similar attacks in the future?",
        "options": [
            "NGFW",
            "WAF",
            "TLS",
            "SD-WAN"
        ],
        "correct_answer": 2,
        "description": "A Web Application Firewall (WAF) protects web applications by filtering and monitoring HTTP traffic between a web application and the Internet."
    },
    {
        "question": "An enterprise is trying to limit outbound DNS traffic originating from its internal network. Outbound DNS requests will only be allowed from one device with the IP address 10.50.10.25. Which of the following firewall ACLs will accomplish this goal?",
        "options": [
            "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53. Access list outbound deny 10.50.10.25/32 0.0.0.0/0 port 53.",
            "Access list outbound permit 0.0.0.0/0 10.50.10.25/32 port 53. Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53.",
            "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53. Access list outbound deny 0.0.0.0/0 10.50.10.25/32 port 53.",
            "Access list outbound permit 10.50.10.25/32 0.0.0.0/0 port 53. Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53."
        ],
        "correct_answer": 3,
        "description": "This rule permits DNS requests only from the IP address 10.50.10.25 while denying others."
    },
    {
        "question": "Which of the following would be the best way to block unknown programs from executing?",
        "options": [
            "Access control list",
            "Application allow list",
            "Host-based firewall",
            "DLP solution"
        ],
        "correct_answer": 2,
        "description": "An application allow list (also known as whitelisting) only allows pre-approved applications to run, blocking unknown or unauthorized programs."
    },
    {
        "question": "A company’s web filter is configured to scan the URL for strings and deny access when matches are found. Which of the following search strings should an analyst employ to prohibit access to non-encrypted websites?",
        "options": [
            "encryption=off",
            "http://",
            "www.*.com",
            ":443"
        ],
        "correct_answer": 2,
        "description": "The search string 'http://' should be used to prohibit access to non-encrypted websites."
    },
    {
        "question": "A systems administrator works for a local hospital and needs to ensure patient data is protected and secure. Which of the following data classifications should be used to secure patient data?",
        "options": [
            "Private",
            "Critical",
            "Sensitive",
            "Public"
        ],
        "correct_answer": 3,
        "description": "Sensitive data classification is appropriate for securing patient data, which requires protection due to privacy regulations like HIPAA."
    },
    {
        "question": "A company is required to use certified hardware when building networks. Which of the following best addresses the risks associated with procuring counterfeit hardware?",
        "options": [
            "A thorough analysis of the supply chain",
            "A legally enforceable corporate acquisition policy",
            "A right to audit clause in vendor contracts and SOWs",
            "An in-depth penetration test of all suppliers and vendors"
        ],
        "correct_answer": 1,
        "description": "A thorough analysis of the supply chain is the best approach to address the risks associated with procuring counterfeit hardware."
    },

# Security Operations

    {
        "question": "Which of the following should a security administrator adhere to when setting up a new set of firewall rules?",
        "options": [
            "Disaster recovery plan",
            "Incident response procedure",
            "Business continuity plan",
            "Change management procedure"
        ],
        "correct_answer": 4,
        "description": "A security administrator should adhere to the change management procedure when setting up new firewall rules."
    },
    {
        "question": "During a security incident, the security operations team identified sustained network traffic from a malicious IP address: 10.1.4.9. A security analyst is creating an inbound firewall rule to block the IP address from accessing the organization’s network. Which of the following fulfills this request?",
        "options": [
            "access-list inbound deny ip source 0.0.0.0/0 destination 10.1.4.9/32",
            "access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0",
            "access-list inbound permit ip source 10.1.4.9/32 destination 0.0.0.0/0",
            "access-list inbound permit ip source 0.0.0.0/0 destination 10.1.4.9/32"
        ],
        "correct_answer": 2,
        "description": "The correct firewall rule to block inbound traffic from the malicious IP address is: access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0."
    },
    {
        "question": "A technician needs to apply a high-priority patch to a production system. Which of the following steps should be taken first?",
        "options": [
            "Air gap the system.",
            "Move the system to a different network segment.",
            "Create a change control request.",
            "Apply the patch to the system."
        ],
        "correct_answer": 3,
        "description": "Creating a change control request is essential before applying patches to ensure proper review and approval of the changes."
    },
    {
        "question": "A company needs to provide administrative access to internal resources while minimizing the traffic allowed through the security boundary. Which of the following methods is most secure?",
        "options": [
            "Implementing a bastion host",
            "Deploying a perimeter network",
            "Installing a WAF",
            "Utilizing single sign-on"
        ],
        "correct_answer": 1,
        "description": "Implementing a bastion host is the most secure method to provide administrative access while minimizing traffic through the security boundary."
    },
    {
        "question": "An administrator was notified that a user logged in remotely after hours and copied large amounts of data to a personal device. Which of the following best describes the user’s activity?",
        "options": [
            "Penetration testing",
            "Phishing campaign",
            "External audit",
            "Insider threat"
        ],
        "correct_answer": 4,
        "description": "An insider threat refers to a security risk that comes from within the organization, such as an employee or contractor who misuses access to company data."
    },
    {
        "question": "Which of the following can be used to identify potential attacker activities without affecting production servers?",
        "options": [
            "Honeypot",
            "Video surveillance",
            "Zero Trust",
            "Geofencing"
        ],
        "correct_answer": 1,
        "description": "A honeypot is a decoy system set up to attract attackers and observe their behavior without impacting the production environment."
    },
    {
        "question": "During an investigation, an incident response team attempts to understand the source of an incident. Which of the following incident response activities describes this process?",
        "options": [
            "Analysis",
            "Lessons learned",
            "Detection",
            "Containment"
        ],
        "correct_answer": 1,
        "description": "Analysis is the process of examining the details of an incident to determine its cause, impact, and any potential vulnerabilities that were exploited."
    },
    {
        "question": "A security practitioner completes a vulnerability assessment on a company’s network and finds several vulnerabilities, which the operations team remediates. Which of the following should be done next?",
        "options": [
            "Conduct an audit.",
            "Initiate a penetration test.",
            "Rescan the network.",
            "Submit a report."
        ],
        "correct_answer": 3,
        "description": "After remediating vulnerabilities, a rescan of the network is necessary to verify that the issues have been properly fixed and no new vulnerabilities have been introduced."
    },

# Security Program Management and Oversight

    {
        "question": "An IT manager informs the entire help desk staff that only the IT manager and the help desk lead will have access to the administrator console of the help desk software. Which of the following security techniques is the IT manager setting up?",
        "options": [
            "Hardening",
            "Employee monitoring",
            "Configuration enforcement",
            "Least privilege"
        ],
        "correct_answer": 4,
        "description": "The IT manager is setting up the least privilege security technique."
    },
    {
        "question": "Which of the following security control types does an acceptable use policy best represent?",
        "options": [
            "Detective",
            "Compensating",
            "Corrective",
            "Preventive"
        ],
        "correct_answer": 4,
        "description": "An acceptable use policy is a preventive control type."
    },
    {
        "question": "A software development manager wants to ensure the authenticity of the code created by the company. Which of the following options is the most appropriate?",
        "options": [
            "Testing input validation on the user input fields",
            "Performing code signing on company-developed software",
            "Performing static code analysis on the software",
            "Ensuring secure cookies are used"
        ],
        "correct_answer": 2,
        "description": "Code signing is the process of digitally signing software to verify its authenticity and integrity, ensuring that it hasn't been tampered with."
    },
    {
        "question": "Which of the following is the most likely to be used to document risks, responsible parties, and thresholds?",
        "options": [
            "Risk tolerance",
            "Risk transfer",
            "Risk register",
            "Risk analysis"
        ],
        "correct_answer": 3,
        "description": "A risk register is used to document risks, responsible parties, and thresholds."
    },
    {
        "question": "Which of the following provides the details about the terms of a test with a third-party penetration tester?",
        "options": [
            "Rules of engagement",
            "Supply chain analysis",
            "Right to audit clause",
            "Due diligence"
        ],
        "correct_answer": 1,
        "description": "Rules of engagement provide the details about the terms of a test with a third-party penetration tester."
    }
]
