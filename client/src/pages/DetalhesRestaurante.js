import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../CSS/DetalhesRestaurante.css';
import Nav from '../components/Nav'; 

function RestauranteDetalhes(props) {
  const [restaurante, setRestaurante] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/restaurantes/${props.match.params.id}`).then(response => {
        setRestaurante(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [props.match.params.id]);

  if (!restaurante) {
    return <div>Carregando...</div>;
  }

  return (
    <div className="restaurante-detalhes">
      <header>
        <Nav /> 
      </header>
      <div className="imagem">
        <img src={restaurante.imagem_url} alt={restaurante.nome} />
      </div>
      <div className="info">
        <h1>{restaurante.nome}</h1>
        <p>{restaurante.endereco}</p>
        <p>{restaurante.cidade}, {restaurante.estado}</p>
        <p>{restaurante.telefone}</p>
        <p>{restaurante.descricao}</p>
      </div>
    </div>
  );
}

export default RestauranteDetalhes;