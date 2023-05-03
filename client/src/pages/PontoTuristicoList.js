import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PontoTuristicoList() {
  const [pontosTuristicos, setPontosTuristicos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/pontos_turisticos').then(response => {
        setPontosTuristicos(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Pontos turísticos</h1>
      {pontosTuristicos.map(pontoTuristico => (
        <div key={pontoTuristico.id}>
          <h2>{pontoTuristico.nome}</h2>
          <p>{pontoTuristico.descricao}</p>
          <p>{pontoTuristico.localizacao}</p>
          <img src={pontoTuristico.imagem_url} alt={pontoTuristico.nome} />
        </div>
        
      ))}

    </div>
  );
}

export default PontoTuristicoList;
