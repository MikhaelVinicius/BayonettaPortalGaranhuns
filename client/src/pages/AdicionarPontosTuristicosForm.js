import { Formik, Form, Field, ErrorMessage } from 'formik';

function AdicionarPontoTuristicoForm() {
  const initialValues = {
    nome: '',
    descricao: '',
    localizacao: '',
    imagem_url: '',
  };

  const onSubmit = (values, { resetForm }) => {
    axios.post('http://127.0.0.1:5000/api/pontos_turisticos', values)
      .then(response => {
        alert('Ponto turístico adicionado com sucesso!');
        resetForm();
      })
      .catch(error => {
        alert('Não foi possível adicionar o ponto turístico.');
      });
  };

  const validate = (values) => {
    const errors = {};

    if (!values.nome) {
      errors.nome = 'O nome do ponto turístico é obrigatório.';
    }

    if (!values.descricao) {
      errors.descricao = 'A descrição do ponto turístico é obrigatória.';
    }

    if (!values.localizacao) {
      errors.localizacao = 'A localização do ponto turístico é obrigatória.';
    }

    return errors;
  };

  return (
    <Formik
      initialValues={initialValues}
      onSubmit={onSubmit}
      validate={validate}
    >
      {({ isSubmitting }) => (
        <Form>
          <div>
            <label htmlFor="nome">Nome:</label>
            <Field type="text" id="nome" name="nome" />
            <ErrorMessage name="nome" component="div" />
          </div>
          <div>
            <label htmlFor="descricao">Descrição:</label>
            <Field as="textarea" id="descricao" name="descricao" />
            <ErrorMessage name="descricao" component="div" />
          </div>
          <div>
            <label htmlFor="localizacao">Localização:</label>
            <Field type="text" id="localizacao" name="localizacao" />
            <ErrorMessage name="localizacao" component="div" />
          </div>
          <div>
            <label htmlFor="imagem_url">URL da imagem:</label>
            <Field type="text" id="imagem_url" name="imagem_url" />
            <ErrorMessage name="imagem_url" component="div" />
          </div>
          <button type="submit" disabled={isSubmitting}>
            Adicionar ponto turístico
          </button>
        </Form>
      )}
    </Formik>
  );
}
