import LoginPage from './Login';
import RegisterPage from './Register';
import './home.css'

function HomePage() {
    return (
        <div className="homepage-container">
            <div className="forms-container">
                <div className="form-item login">
                    <LoginPage />
                </div>
                <div className="form-item">
                    <RegisterPage />
                </div>
            </div>
        </div>
    );
}

export default HomePage;
