<script>
	 import {
        Alert,
        Container,
        Styles,
        Button,
        Table,
    } from 'sveltestrap';

	let header = "Probando svelte";
    let posts = [];
    let renderLocalAPI = false;
    let responseData = [];

	const getPet = async () => {
        renderLocalAPI = true;
        const url = 'http://127.0.0.1:8000/Listar-Mascotas/';
        const config = {
            method: 'GET',
			mode: 'no-cors',
        };
        const response = await fetch(url,config);
	
        responseData = await response.json();
    }



</script>

<main>
	<Container>
		<h1>{header}</h1>
        <p> Este es un elemento p</p>
        <Table bordered>
            <thead>
              <tr>
                <th>{ renderLocalAPI ? 'id' : 'UserId'}</th>
                <th>{ renderLocalAPI ? 'name2' : 'id'}</th>
                <th>{ renderLocalAPI ? 'age' : 'title'}</th>
              </tr>
            </thead>
            <tbody>
              {#each responseData as data}
                <tr>
					
                    <td>{ renderLocalAPI ? data.id : data.userId}</td>
                    <td>{ renderLocalAPI ? data.name2 : data.id}</td>
                    <td>{ renderLocalAPI ? data.age : data.title}</td>
                </tr>
              {/each}
            </tbody>
          </Table>
		  <Button color='primary' on:click={getPet}> Obtener pets (API LOCAL)</Button>
	</Container>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>