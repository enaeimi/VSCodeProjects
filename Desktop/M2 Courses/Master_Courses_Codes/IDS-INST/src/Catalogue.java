import java.util.*;


public class Catalogue{

	private ArrayList<Person> personCatalogue ;
	
	public Catalogue(){
	
		this.personCatalogue =  new ArrayList<Person>();
	}
	
	public Catalogue(int numberOfPersons){
		
		this.personCatalogue = new ArrayList<Person>(numberOfPersons);
	}
	
	public ArrayList<Person> getPersonCatalogue(){
	
		return this.personCatalogue;
	}
	
	public void setPersonCatalogue(ArrayList<Person> persons){
	
		this.personCatalogue = persons;
	}
	
	public boolean register(Person person){
	
		if(this.personCatalogue.add(person))
			return true;
		else
			return false;
	}
	
	public void update(Person person){
	
		Iterator<Person> iterator = this.personCatalogue.iterator();
		
		while(iterator.hasNext() == true){
			
			if(iterator.next().getPersonId() == person.getPersonId()){
				iterator.remove();
			}
		}
		
		this.personCatalogue.add(person);
	}
	
	public void delete(Person person){
		
		Iterator<Person> iterator = this.personCatalogue.iterator();
		
		while(iterator.hasNext() == true){
			
			if(iterator.next().getPersonId() == person.getPersonId()){
				iterator.remove();
			}
		}
	}
	
}