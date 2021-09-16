package ProjectsList;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.GregorianCalendar;

public class newProjectDialog extends JDialog implements ActionListener {

    private Project project;
    private JCheckBox buttonRemoved;
    private JTextField txtTitle;
    private JTextField txtDescription;
    private JTextField txtReasonForRemoval;
    private JTextField txtTags;
    private JTextField txtVariations;
    private JTextField txtResources;

    private JButton okButton;
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

    public newProjectDialog(JFrame parent, Project project) {
        // call parent and create a 'modal' dialog
        super(parent, true);

        this.project = project;
        setTitle("Adding a Project");
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
        txtTitle = new JTextField("Queen Placements");
        buttonRemoved = new JCheckBox();
        buttonRemoved.setSelected(false);
        txtDescription = new JTextField("Non-attacking placements of queens on a chess board");
        txtReasonForRemoval = new JTextField("N/A");
        txtTags = new JTextField("Chess, discrete, queens");
        txtVariations = new JTextField("rectangle boards, other pieces");
        txtResources = new JTextField("n-Queens problem");

        c.gridy = 0;
        c.gridx = 0;

        textPanel.add(new JLabel("Title: "), c); c.gridy++;
        textPanel.add(new JLabel("Description: "), c); c.gridy++;
        textPanel.add(new JLabel("Tags: "), c); c.gridy++;
        textPanel.add(new JLabel("Variations: "), c); c.gridy++;
        textPanel.add(new JLabel("Resources: "), c); c.gridy++;
        textPanel.add(new JLabel("Removed?: "), c); c.gridy++;
        textPanel.add(new JLabel("Reason for Removal: "), c); c.gridy++;

        c.gridx = 1;
        c.gridy = 0;

        textPanel.add(txtTitle, c); c.gridy++;
        textPanel.add(txtDescription, c); c.gridy++;
        textPanel.add(txtTags, c); c.gridy++;
        textPanel.add(txtVariations, c); c.gridy++;
        textPanel.add(txtResources, c); c.gridy++;
        textPanel.add(buttonRemoved, c); c.gridy++;
        textPanel.add(txtReasonForRemoval, c);

        getContentPane().add(textPanel, BorderLayout.WEST);

        // Instantiate and display two buttons
        okButton = new JButton("OK");
        cancelButton = new JButton("Cancel");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(okButton);
        buttonPanel.add(cancelButton);
        getContentPane().add(buttonPanel, BorderLayout.SOUTH);
        okButton.addActionListener(this);
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
        if (button == okButton) {
            // save the information in the object
            closeStatus = OK;

            project.setTitle(txtTitle.getText());
            project.setDescription(txtDescription.getText());
            project.setReasonForRemoval(txtReasonForRemoval.getText());
            project.setTags(txtTags.getText().split(", "));
            project.setVariations(txtVariations.getText().split(", "));
            project.setResources(txtResources.getText().split(", "));
            project.setRemoved(buttonRemoved.isEnabled());
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
