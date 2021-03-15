<template>
  <div>
    <h2 class="centralizado">{{ titulo }}</h2>
    <table>
      <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Aniversário</th>
        <th>Opções</th>
      </tr>

        <slot> </slot>

    </table>
  </div>
</template>

<script>
export default {
  props: ["titulo"],
};
</script>

<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

.centralizado {
  text-align: center;
}
</style>
