export function formatDate(dateToFormat,needTime){
  let date = new Date(dateToFormat);
	let day = date.getDate(); // Dan u mesecu (1-31)
	let month = date.getMonth() + 1; // Mesec (1-12), zato što je `getMonth()` 0-indeksiran
	let year = date.getUTCFullYear(); // Godina (četvorka)
	let time = date.getUTCHours();
  

  if(needTime){
    let formattedDate=`${day}.${month}.${year}, ${time}h`
    return formattedDate
  }

  else{
    let formattedDate=`${day}.${month}.${year}`
    console.log(formatDate)
	  return formattedDate
  }

  
  
}