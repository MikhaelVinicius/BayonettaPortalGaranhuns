import React from 'react';
import { Button } from 'react-bootstrap';

function Hero() {
  return (
    <div className="hero">
      <img src="/img/destaque.jpg" alt="Destaque" />
      <Button variant="danger" href="#">Explore os pontos turísticos</Button>
    </div>
  );
}

export default Hero;
