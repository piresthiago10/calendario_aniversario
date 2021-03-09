<template>
  <div>
    <table>
      <tr>
        <th>Id</th>
        <th>Nome</th>
        <th>Data de Aniversário</th>
      </tr>
      <tr v-for="aniversario of aniversarios">
        <!-- {{aniversarios.nome}}
      {{aniversarios.data_aniversario}}  -->
        <td>01</td>
        <td>Teste</td>
        <td>01/01/1999</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      aniversarios: [],
    };
  },

  created() {
    this.$http
      .get("https://swapi.dev/api/planets/")
      .then((res) => res.json())
      .then(
        (aniversarios) => (this.aniversarios = aniversarios),
        (err) => console.log(err)
      );
  },
};
</script>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
