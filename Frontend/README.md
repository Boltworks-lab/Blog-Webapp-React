# React + Vite

# Blog-Webapp-React
A blog webapp made using react for the frontend and python with django for the backend
## ![Features Icon](https://img.icons8.com/ios-filled/50/000000/list.png "Features") Features

### Core Features
- **Onboarding Pages**:
  - Home page of the blog app, including post in seperate paginations, caterogies and latest news.
  - Navigation menu of the different pages of the blog webapp

- **Authentication Pages**:
  - **Login**: Secure login with validation.
  - **Register**: User registration form with basic field validations.

- **Blog core features**:
  - Create new posts, edit a post, see list of posts.
  - See comments of posts, make replies, like posts, bookmark posts.
  - Receive activity notifications of comments, likes, and bookmarks

- **User-Friendly Interface**:
  - UI IS responsive across different screen sizes.
  - simple and user friendly

---

## ![Tech Stack Icon](https://img.icons8.com/color/48/000000/system-task.png "Tech Stack") Tech Stack
- **Frontend**: React + Vite  
- **Styling**: Bootstrap, CSS  
- **State Management**: React useState  
- **Routing**: React Router  
- **Authentication**: useAuthStore anf JWT authentification
- **Version Control**: Git + GitHub  

---

## ![Setup Icon](https://img.icons8.com/color/48/000000/settings.png "Setup") Installation

### Prerequisites
- Node.js (v16 or higher)
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Boltworks-lab/Blog-Webapp-React.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Frontend
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the development server:
   ```bash
   npm run dev
   ```
5. Open your browser and navigate to:
   ```text
   http://localhost:5173
   ```

---

## ![Structure Icon](https://img.icons8.com/dusk/64/000000/folder-invoices.png "Folder Structure") Project Structure
```
src/
├── assets/          # Static files (images and logos)
├── layouts/         # Mainwrapper and private route (useState, navigate and useAuthStore from React-dom)
├── plugins/         # Moment, Toast and useUserData (for current dates and success alerts settings)
├── store/           # Authentifications (useUserData)
├── utils/           #Auth config, axios
├── views/           # React Components (Headers, footers, dashboard, posts)
├── App.css/         # Styling for App.jsx
├── App.jsx          # Main app component
├── index.css/       # Styling for index.jsx
├── main.jsx         # Entry point for Vite


```

---

## ![Team Icon](https://img.icons8.com/color/48/000000/conference-call.png "Team") Team Members
- **Group P**  
1. **Omoikhunu Ohigwere Mark**
    LCU/UG/23/26884 - Software Engineering

2. **Chikwe Victor**  
   LCU/UG/22/23797 - Computer Science  

3. **Fashina Fuad Ayomide**  
   LCU/UG/22/21742 - Information Technology  

4. **Agu Lotanna**  
   LCU/UG/22/24037 -  Computer Science

5. **Badmus Habeeb Abidemi**  
   LCU/UG/21/19848 - Computer Science  

6. **Ojo Emmanuel Temitope**  
   LCU/UG/21/19658 -   Software Engineering

7. **Aderinto Mursuq Muhammed**
    LCU/UG/20/16605 - Computer science with electronics

8. **Alausa Adebukola Adedamilola**
    LCU/UG/21/19852 - Computer science 

 


---

## ![Course Icon](https://img.icons8.com/external-flat-juicy-fish/48/000000/external-book-education-flat-flat-juicy-fish.png "Course") Course Information
- **Course Code**: GST 306  
- **Project Title**: Blog Webapp  

---

## ![Contribute Icon](https://img.icons8.com/fluency/48/000000/pull-request.png "Contribute") Contribution Guidelines
1. Fork the repository and create a new branch for your feature:
   ```bash
   git checkout -b <feature-name>
   ```
2. Commit your changes:
   ```bash
   git commit -m "Add <feature>"
   ```
3. Push to the branch:
   ```bash
   git push origin <feature-name>
   ```
4. Submit a pull request for review.

---

## ![License Icon](https://img.icons8.com/color/48/000000/copyright.png "License") License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## ![Heart Icon](https://img.icons8.com/emoji/48/000000/red-heart.png "Built with Love") Acknowledgments
Special thanks to our lecturer for the project guidelines and our teammates for their dedication and effort.

---

Built by **Group P**.
```

---


This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
