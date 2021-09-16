package ProjectsList;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class removeProjectDialog extends JDialog implements ActionListener {

    private Project project;
    private JLabel txtTitle;
    private JLabel txtDescription;
    private JTextField txtReasonForRemoval;

    private JButton removeButton;
    private JButton cancelButton;
    private int closeStatus;
    static final int OK = 0;
    static final int CANCEL = 1;

    /*********************************************************
     Instantiate a Custom Dialog as 'modal' and wait for the
     user to provide data and click on a button.

     @param parent reference to the JFrame application
     @param project an instantiated object to be filled with data
     *********************************************************/

    public removeProjectDialog(JFrame parent, Project project) {
        // call parent and create a 'modal' dialog
        super(parent, true);

        this.project = project;
        setTitle("Removing a Project");
        closeStatus = CANCEL;
        setSize(600,400);

        JPanel textPanel = new JPanel();
        textPanel.setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        c.weightx = 1;
        c.weighty = 1;
        c.fill = GridBagConstraints.HORIZONTAL;

        // prevent user from closing window
        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);

        // instantiate and display two text fields
        txtTitle = new JLabel(project.getTitle());
        txtDescription = new JLabel(project.getDescription());
        txtReasonForRemoval = new JTextField("");

        c.gridy = 0;
        c.gridx = 0;

        textPanel.add(new JLabel("Title: "), c); c.gridy++;
        textPanel.add(new JLabel("Description: "), c); c.gridy++;
        textPanel.add(new JLabel("Reason for Removal: "), c); c.gridy++;

        c.gridx = 1;
        c.gridy = 0;

        textPanel.add(txtTitle, c); c.gridy++;
        textPanel.add(txtDescription, c); c.gridy++;
        textPanel.add(txtReasonForRemoval, c);

        getContentPane().add(textPanel, BorderLayout.WEST);

        // Instantiate and display two buttons
        removeButton = new JButton("Remove");
        cancelButton = new JButton("Cancel");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(removeButton);
        buttonPanel.add(cancelButton);
        getContentPane().add(buttonPanel, BorderLayout.SOUTH);
        removeButton.addActionListener(this);
        cancelButton.addActionListener(this);

        pack();
        setVisible (true);
    }

    /**************************************************************
     Respond to either button clicks
     @param e the action event that was just fired
     **************************************************************/
    public void actionPerformed(ActionEvent e) {

        JButton button = (JButton) e.getSource();

        // if OK clicked then fill the object
        if (button == removeButton) {
            // save the information in the object
            closeStatus = OK;

            project.setRemoved(true);
            project.setReasonForRemoval(txtReasonForRemoval.getText());
        }

//        if (button == cancelButton){
//            // pass
//        }

        // make the dialog disappear
        dispose();
    }

    /**************************************************************
     Return a String to let the caller know which button
     was clicked

     @return an int representing the option OK or CANCEL
     **************************************************************/
    public int getCloseStatus(){
        return closeStatus;
    }
}
