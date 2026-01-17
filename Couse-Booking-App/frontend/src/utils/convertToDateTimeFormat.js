export function convertToDateTimeFormat(dateTimeString) {
	const date = new Date(dateTimeString);
	const year = date.getFullYear();
	const month = String(date.getMonth() + 1).padStart(2, "0"); // Dodaj nulu ako je mesec jednocifren
	const day = String(date.getDate()).padStart(2, "0"); // Dodaj nulu ako je dan jednocifren
	const hours = String(date.getHours()).padStart(2, "0"); // Dodaj nulu ako je sat jednocifren
	const minutes = String(date.getMinutes()).padStart(2, "0"); // Dodaj nulu ako su minuti jednocifreni

	return `${year}-${month}-${day}T${hours}:${minutes}`;
}