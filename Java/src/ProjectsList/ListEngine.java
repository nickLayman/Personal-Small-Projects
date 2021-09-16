package ProjectsList;

import javax.swing.table.AbstractTableModel;
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

/************************************************************************
 * This program builds a GUI that works as a car/truck registry.
 * Multiple functions are used to allow the user to buy, sell, and view
 * their inventory
 *
 * @author Justin Von Kulajta Winn and Nick Layman
 * @version 1.8
 ************************************************************************/
public class ListEngine extends AbstractTableModel {

    /** this is Array List that holds all of the autos in the inventory */
    private ArrayList<Project> listProjects;

    /** this is the Array List that holds all of the autos displayed on the GUI */
    private ArrayList<Project> filteredListProjects;

    /** this is a sorted list of the most used tags in the filtered list */
    private ArrayList<String> topTags;

    /** this is the array for the column names in the bought screen */
    private String[] columnNamesProjects = {"Title", "Description",
            "Top Tags", "Variations", "Resources"};

    /** this is the array for the column names in the sold screen */
    private String[] columnNamesRemoved = {"Title", "Description",
            "Reason for Removal", "Top Tags", "Variations", "Resources"};

    /** this is the variable representing the bought screen */
    public final int projectScreen = 0;

    /** this is the variable representing the sold screen */
    public final int removedScreen = 1;

    /** this is the variable representing the current display screen */
    public int displayValue;

    /************************************************************************
     * This is a function that overrides the abstract function is the super
     * class. It returns the name of whatever screen is being displayed.
     * @param col is the column number sent to the function
     * @return the name of the column of whatever screen is being displayed
     ************************************************************************/
    @Override
    public String getColumnName(int col) {
        switch(displayValue){
            case projectScreen:
                return columnNamesProjects[col];

            case removedScreen:
                return columnNamesRemoved[col];

            default:
                throw new RuntimeException("JTable col out of range: " + col);
        }
    }

    /************************************************************************
     * This is the constructor of the class. It creates an the arrayList
     * 'listAutos' and the calls a function to add to the list. It then
     * updates the display to sort the vehicles.
     ************************************************************************/
    public ListEngine() {
        super();
        listProjects = new ArrayList<Project>();
        loadFromText(".\\src\\ProjectsList\\ProjectsUse.txt");
        createList();
    }

    /************************************************************************
     * This function updates the display to choose which screen is to be
     * displayed. It then sorts the arrayList appropriately.
     * @param pDisplayValue is the value of the screen that is to be displayed
     ************************************************************************/
    public void updateDisplay(int pDisplayValue){
        displayValue = pDisplayValue;

        if (displayValue == projectScreen) {
            filteredListProjects = (ArrayList<Project>) listProjects.stream()
                    .filter(arg -> !arg.isRemoved())
                    .collect(Collectors.toList());
            filteredListProjects.sort(Comparator.comparing(o ->
                    o.getTitle().toUpperCase()));
        }

        else if (displayValue == removedScreen) {
            filteredListProjects = (ArrayList<Project>) listProjects.stream()
                    .filter(Project::isRemoved)
                    .collect(Collectors.toList());
            filteredListProjects.sort(Comparator.comparing(o ->
                    o.getTitle().toUpperCase()));
        }

        else
            filteredListProjects = listProjects;

        ArrayList<String> allTags = new ArrayList<String>();
        for (Project proj : filteredListProjects){
            Collections.addAll(allTags, proj.getTags());
        }

        topTags = new ArrayList<String>();
        for (String tag : allTags){
            if (!topTags.contains(tag))
                topTags.add(tag);
        }

        topTags.sort(Comparator.comparing(o -> -Collections.frequency(allTags, o)));

        fireTableDataChanged();
        fireTableStructureChanged();
    }

    /************************************************************************
     * This function adds an auto to the arraylist that holds the cars in
     * the user's inventory
     * @param a is the auto that is to be added to the arrayList
     ************************************************************************/
    public void add(Project a) {
        listProjects.add(a);
        listProjects.sort(Comparator.comparing(o ->
                o.getTitle().toUpperCase()));
        fireTableDataChanged();
    }

    /************************************************************************
     * This function returns the the auto at location 'i' in the arrayList
     * @param i is the location in the arrayList of the desired auto
     * @return the auto at location 'i' in the arrayList
     ************************************************************************/
    public Project get(int i) {
        return filteredListProjects.get(i);
    }

    /************************************************************************
     * This function returns the size of the arrayList
     * @return the size of the arrayList
     ************************************************************************/
    public int getSize() {
        return filteredListProjects.size();
    }

    /************************************************************************
     * This function returns how many rows are in the J Table
     * @return the number of rows in the J Table
     ************************************************************************/
    @Override
    public int getRowCount() {
        return filteredListProjects.size();
    }

    /************************************************************************
     * This function gets the number of columns in the J Table
     * @return the number of columns depending on which screen you are
     *         currently on
     ************************************************************************/
    @Override
    public int getColumnCount() {
        switch(displayValue){
            case projectScreen:
                return columnNamesProjects.length;
            case removedScreen:
                return columnNamesRemoved.length;
            default:
                throw new RuntimeException("JTable Column Count Error");
        }
    }

    /************************************************************************
     * This function returns the object at a specific location using a
     * coordinate system.
     * @param col is the column number that is wanted by the user
     * @param row is the row number that is wanted by the user
     * @return the object at the desired location
     ************************************************************************/
    @Override
    public Object getValueAt(int row, int col) {
        switch (col) {
            case 0:
                return filteredListProjects.get(row).getTitle();

            case 1:
                return filteredListProjects.get(row).getDescription();

            case 2:
                if (displayValue == projectScreen) {
                    List<String> projTags = Arrays.asList(filteredListProjects.get(row).getTags());
                    List<String> projTopTags = new ArrayList<String>();
                    StringBuilder tagString = new StringBuilder();
                    for (String s : topTags) {
                        if (projTopTags.size() < 3 && projTags.contains(s))
                            projTopTags.add(s);
                    }
                    for (String s : projTopTags)
                        tagString.append(s).append(", ");
                    return tagString.toString().substring(0, tagString.length() - 2);
                }
                if (displayValue == removedScreen)
                    return filteredListProjects.get(row).getReasonForRemoval();

            case 3:
                if (displayValue == projectScreen) {
                    String[] vars = filteredListProjects.get(row).getVariations();
                    StringBuilder varString = new StringBuilder();
                    for (String s : vars) {
                        varString.append(s).append(", ");
                    }
                    return varString.toString().substring(0, varString.length() - 2);
                }
                else if (displayValue == removedScreen) {
                    List<String> projTags = Arrays.asList(filteredListProjects.get(row).getTags());
                    List<String> projTopTags = new ArrayList<String>();
                    StringBuilder tagString = new StringBuilder();
                    for (String s : topTags) {
                        if (projTopTags.size() < 3 && projTags.contains(s))
                            projTopTags.add(s);
                    }
                    for (String s : projTopTags)
                        tagString.append(s).append(", ");
                    return tagString.toString().substring(0, tagString.length() - 2);
                }

            case 4:
                if (displayValue == projectScreen) {
                    String[] res = filteredListProjects.get(row).getResources();
                    StringBuilder resString = new StringBuilder();
                    for (String s : res) {
                        resString.append(s).append(", ");
                    }
                    return resString.toString().substring(0, resString.length() - 2);
                }
                if (displayValue == removedScreen) {
                    String[] vars = filteredListProjects.get(row).getVariations();
                    StringBuilder varString = new StringBuilder();
                    for (String s : vars) {
                        varString.append(s).append(", ");
                    }
                    return varString.toString().substring(0, varString.length() - 2);
                }

            case 5:
                if (displayValue == removedScreen) {
                    String[] vars = filteredListProjects.get(row).getVariations();
                    StringBuilder varString = new StringBuilder();
                    for (String s : vars) {
                        varString.append(s).append(", ");
                    }
                    return varString.toString().substring(0, varString.length() - 2);
                }

            default:
                throw new RuntimeException("JTable row,col out of range: " +
                        row + " " + col);
        }
    }

    /************************************************************************
     * This function saves the arrayList into a file. It breaks up each
     * car and truck into each of their elements. It first saves the number
     * of vehicles, then goes through the array and saves each component of
     * every car and truck.
     * @param filename is the name of the file that the data will be saved
     *                 into
     ************************************************************************/
    public boolean saveAsText(String filename) {
        if (filename.equals(""))
            return false;
        try {
            PrintStream out = new PrintStream(new FileOutputStream(filename));

//            out.println(listProjects.size());
//            out.println();

            for (Project proj : listProjects) {
                if (proj.isRemoved())
                    out.println("*removed*");
                out.println("Title: " + proj.getTitle());
                out.println("Description: " + proj.getDescription());
                if (proj.isRemoved())
                    out.println("Reason for Removal: " + proj.getReasonForRemoval());
                else
                    out.println("Reason for Removal: N/A");
                out.println("Tags: " + Arrays.toString(proj.getTags()));
                out.println("Variations: " + Arrays.toString(proj.getVariations()));
                out.println("Resources: " + Arrays.toString(proj.getResources()));
                out.println();
            }
        }
        catch (Exception e) {
            //pop up window saying it does not work
        }
        return true;
    }

    /************************************************************************
     * This function loads every car and truck from the file. The function
     * first finds the number of vehicles and then saves all data needed for
     * creating each truck and car
     * @param filename is the name of the file that the data will be loaded
     *                 in from
     ************************************************************************/
    // TODO: Make this more robust. without number at top. Without very specific order.
    public void loadFromText(String filename) {
        listProjects.clear();
        try {
            if (filename == null || filename.equals("")) {
                // hopefully unreachable
                throw new Exception();
            }

            BufferedReader read = new BufferedReader(new FileReader(filename));

            int length = Integer.parseInt(read.readLine());

            for (int i = 0; i < length; i++) {
                read.readLine();
                Project proj = new Project();
                String firstLine = read.readLine();
                if (firstLine.contains("*removed*")) {
                    proj.setRemoved(true);
                    proj.setTitle(read.readLine().substring(7)); // substring takes out "Title: "
                }
                else {
                    proj.setRemoved(false);
                    proj.setTitle(firstLine.substring(7));
                }

                proj.setDescription(read.readLine().substring(13));
                proj.setReasonForRemoval(read.readLine().substring(20));
                proj.setTags(read.readLine().substring(6).split(", "));
                proj.setVariations(read.readLine().substring(12).split(", "));
                proj.setResources(read.readLine().substring(11).split(", "));
                add(proj);
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }

    /************************************************************************
     * This function creates a starting list that starts the display with
     * 6 vehicles. 3 cars and 3 trucks are created.
     ************************************************************************/
    public void createList() {
        Project project1 = new Project("Non-attacking Queen and Rook Placements");
        project1.setRemoved(false);
        project1.setDescription("Find all possible placements of non-attacking queens and rooks");
        project1.setReasonForRemoval("N/A");
        project1.setTags(new String[]{"this", "is", "an", "array", "this", "this", "discrete"});
        project1.setResources(new String[]{"none"});
        project1.setVariations(new String[]{"rectangles"});

        add(project1);
    }
}