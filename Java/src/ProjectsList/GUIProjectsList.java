package ProjectsList;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/*****************************************************************
 *
 * Maintains the GUI1024 for the red box rental store
 *
 *****************************************************************/
public class GUIProjectsList extends JFrame implements ActionListener{
    /** Holds menu bar */
    private JMenuBar menus;

    /** menus in the menu bar */
    private JMenu fileMenu;
    private JMenu viewMenu;
    private JMenu actionMenu;

    /** items in file menu */
    private JMenuItem saveText;
    private JMenuItem loadText;
    private JMenuItem exitItem;

    /** items in view menu */
    private JMenuItem projectsView;
    private JMenuItem removedView;

    /** items in action menu */
    private JMenuItem viewProject;
    private JMenuItem addProject;
    private JMenuItem removeProject;

    /** Holds the list engine */
    private ListEngine DList;
    private JPanel panel;

    /** Holds JListArea */
    private JTable JListArea;

    /** Scroll pane */
    private JScrollPane scrollList;

    /*****************************************************************
     *
     * A constructor that starts a new GUI1024 for the rental store
     *
     *****************************************************************/
    public GUIProjectsList(){
        //adding menu bar and menu items
        menus = new JMenuBar();

        fileMenu = new JMenu("File");
        viewMenu = new JMenu("View");
        actionMenu = new JMenu("Action");

        saveText = new JMenuItem("Save Text File");
        loadText = new JMenuItem("Load Text File");
        exitItem = new JMenuItem("Exit");

        projectsView = new JMenuItem("Projects");
        removedView = new JMenuItem("Removed Projects");

        viewProject = new JMenuItem("View Project");
        addProject = new JMenuItem("Add Project");
        removeProject = new JMenuItem("Remove Project");

        //adding items to bar
        fileMenu.add(saveText);
        fileMenu.add(loadText);
        fileMenu.add(exitItem);

        viewMenu.add(projectsView);
        viewMenu.add(removedView);

        actionMenu.add(viewProject);
        actionMenu.add(addProject);
        actionMenu.add(removeProject);

        menus.add(fileMenu);
        menus.add(viewMenu);
        menus.add(actionMenu);

        //adding actionListener
        saveText.addActionListener(this);
        loadText.addActionListener(this);
        exitItem.addActionListener(this);

        projectsView.addActionListener(this);
        removedView.addActionListener(this);

        viewProject.addActionListener(this);
        addProject.addActionListener(this);
        removeProject.addActionListener(this);


        setJMenuBar(menus);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        panel = new JPanel();
        DList = new ListEngine();
        DList.updateDisplay(DList.projectScreen);
        JListArea = new JTable(DList);
        scrollList = new JScrollPane(JListArea);
        scrollList.setPreferredSize(new Dimension(1000,300));
        panel.add(scrollList);

        add(panel, BorderLayout.CENTER);

        setVisible(true);
        setSize(1100,450);
    }

    /*****************************************************************
     *
     * This method handles event-handling code for the GUI1024
     *
     * @param e - Holds the action event parameter
     *****************************************************************/
    public void actionPerformed(ActionEvent e) {

        Object selection = e.getSource();

        if (selection == saveText) {
            JFileChooser chooser = new JFileChooser(".\\src\\ProjectsList\\");
            int status = chooser.showSaveDialog(null);
            if (status == JFileChooser.APPROVE_OPTION) {
                String filename = chooser.getSelectedFile().getAbsolutePath();
                DList.saveAsText(filename);
            }
        }

        if (selection == loadText){
            JFileChooser chooser = new JFileChooser(".\\src\\ProjectsList\\");
            int status = chooser.showSaveDialog(null);
            if (status == JFileChooser.APPROVE_OPTION) {
                String filename = chooser.getSelectedFile().getAbsolutePath();
                DList.loadFromText(filename);
            }
            DList.updateDisplay(DList.projectScreen);
        }

        if (selection == exitItem) {
            int dialogResult = JOptionPane.showConfirmDialog (null,
                    "Would You Like to Save your Projects first?","Warning",
                    JOptionPane.YES_NO_OPTION);
            if(dialogResult == JOptionPane.NO_OPTION)
                System.exit(-1);
        }

        if (selection == projectsView){
            DList.updateDisplay(DList.projectScreen);
        }

        if (selection == removedView){
            DList.updateDisplay(DList.removedScreen);
        }

        if (selection == viewProject){
            int index = JListArea.getSelectedRow();
            if (index >= 0) {
                Project proj = DList.get(index);
                projectDisplay display = new projectDisplay(this, proj);
            }
        }

        if (selection == addProject){
            Project proj = new Project();
            newProjectDialog dialog = new newProjectDialog(this, proj);
            if(dialog.getCloseStatus() == newProjectDialog.OK)
                DList.add(proj);
            DList.updateDisplay(DList.displayValue);
        }

        if (selection == removeProject){
            int index = JListArea.getSelectedRow();
            if (index >= 0) {
                Project proj = DList.get(index);
                removeProjectDialog dialog = new removeProjectDialog(this, proj);
                DList.updateDisplay(DList.displayValue);
            }
            else
                JOptionPane.showMessageDialog(null, "Please select a project to remove");
        }
    }

    public static void main(String[] args) {
        new GUIProjectsList();
    }
}