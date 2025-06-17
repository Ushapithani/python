import React from 'react'

const cricket = (props) => {
  console.log("props",props)
  console.log("target",target.props)
S
  const [runs,setruns]=useState(0);
  const [wickets,setwickets]=useState(0);

  const [targer,settarget]=useState(0);
  const handlesix=()=>{
    setruns(runs+6);

  };
  const handlefour=()=>
  {
    setruns(runs+4);
  };
  const handleone=()=>
  {
    setruns(runs+1);
  };
  const handlewickets=()=>
  {
    setruns(runs+1);
    if (wickets+1==10)
      alert("game over")
  };
  return (
    <>
    
      <h1>score :{runs} /{wickets}</h1>
      {
        wickets < 10 ?
      
      <div>

        
      <button onClick={ handlesix}>six</button>
      <button onClick={ handlefour}>four</button>
      <button onClick={ handleone}>one</button>
      <button onClick={ handlewickets}>wicket</button>

        


      </div>
      :
          <h2> GAME IS OVER</h2>

      }
      
      </>
  )
}

export default cricket