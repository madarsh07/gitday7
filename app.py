import java.util.ArrayList;
import java.util.Scanner;

class Contact {
    String name;
    String phone;

    Contact(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }

    void display() {
        System.out.println("Name: " + name + ", Phone: " + phone);
    }
}

public class ContactManager {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Contact> contacts = new ArrayList<>();

        while (true) {
            System.out.println("\n1. Add Contact\n2. View Contacts\n3. Exit");
            System.out.print("Enter choice: ");
            int choice = scanner.nextInt();

