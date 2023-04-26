import { Navbar, Nav, Container, Button } from 'react-bootstrap';
import './PointsOfInterest.css';


function PointsOfInterest() {
    return (
      <div className="points-of-interest">
        <h2>Pontos Turísticos</h2>
        <ul>
          <li>
            <img src="/img/ponto1.jpg" alt="Ponto 1" />
            <h3>Ponto 1</h3>
            <p>Descrição do Ponto 1.</p>
          </li>
          <li>
            <img src="/img/ponto2.jpg" alt="Ponto 2" />
            <h3>Ponto 2</h3>
            <p>Descrição do Ponto 2.</p>
          </li>
          <li>
            <img src="/img/ponto3.jpg" alt="Ponto 3" />
            <h3>Ponto 3</h3>
            <p>Descrição do Ponto 3.</p>
          </li>
        </ul>
      </div>
    );
  }

  export default PointsOfInterest;
