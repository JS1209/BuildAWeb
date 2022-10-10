export default function MakeHouse ({props}) {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>{props.founder}</p>
      <p>{props.animal}</p>
      <p>{props.colors}</p>
    </div>
  );
};
