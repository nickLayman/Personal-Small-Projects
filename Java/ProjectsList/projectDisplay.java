package ProjectsList;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/************************************************************************
 *  This program allows users to purchase a truck and makes sure users
 *  enter valid entries.
 *
 * @author Justin Von Kulajta Winn and Nick Layman
 * @version 1.8
 ************************************************************************/

public class projectDisplay extends JDialog implements ActionListener {
    /** This is the button that represents the 'ok' button */
    private JButton okButton;

    /** This is the integer that represents if the window should close or not */
    private int closeStatus;

    /** This is the integer that represents the action of the OK being pressed */
    static final int OK = 0;

    /** This is the integer that represents the action of the CANCEL being pressed */
    static final int CANCEL = 1;

    /************************************************************************
     * Instantiate a Custom Dialog as 'modal' and wait for the
     * user to provide data and click on a button.
     * @param parent reference to the JFrame application
     * @param project an instantiated object to be filled with data
     ************************************************************************/
    public projectDisplay(JFrame parent, Project project) {
        setTitle("Project Information");
        closeStatus = CANCEL;
        setSize(500,300);
        JPanel textPanel = new JPanel();

        // instantiate and display two text fields
        JLabel txtRemoved = new JLabel(project.isRemoved ? "*removed*" : "");
        JLabel txtTitle = new JLabel("Title: " + project.getTitle());
        JLabel txtDescription = new JLabel("Description: " + project.getDescription());
        JLabel txtReasonForRemoval = new JLabel("Reason for Removal: " + project.getReasonForRemoval());


        StringBuilder tagString = new StringBuilder();
        for (String tag : project.getTags())
            tagString.append(tag).append(", ");
        JLabel txtTags = new JLabel("Tags: " + tagString.toString().substring(0, tagString.length()-2));

        StringBuilder varString = new StringBuilder();
        for (String var : project.getVariations())
            varString.append(var).append(", ");
        JLabel txtVariations = new JLabel("Variations: " + varString.toString().substring(0, varString.length()-2));

        StringBuilder resString = new StringBuilder();
        for (String res : project.getResources())
            resString.append(res).append(", ");
        JLabel txtResources = new JLabel("Resources: " + resString.toString().substring(0, resString.length()-2));


        textPanel.setLayout(new GridLayout(7,1));

        textPanel.add(txtRemoved);
        textPanel.add(txtTitle);
        textPanel.add(txtDescription);
        textPanel.add(txtReasonForRemoval);
        textPanel.add(txtTags);
        textPanel.add(txtVariations);
        textPanel.add(txtResources);

        getContentPane().add(textPanel, BorderLayout.WEST);

        // Instantiate and display two buttons
        okButton = new JButton("OK");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(okButton);
        getContentPane().add(buttonPanel, BorderLayout.SOUTH);
        okButton.addActionListener(this);

        setVisible (true);
    }

    /************************************************************************
     * This function activates when a button has been pressed on the dialog
     * box
     * @param e is used to check what button has been pressed
     ***********************************************************************/
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == okButton) {
            closeStatus = OK;
            dispose();
        }
    }

    /************************************************************************
     * This function returns the current close status
     * @return the integer representing the current close status
     ***********************************************************************/
    public int getCloseStatus(){
        return closeStatus;
    }
}