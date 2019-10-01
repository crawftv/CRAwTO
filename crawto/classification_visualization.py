import sklearn
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, auc, roc_auc_score
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.utils.multiclass import unique_labels
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
"""
IMPORTANT must upgrade Seaborn to use in google Colab.
Classification_report is just the sklearn classification report
Classification_report will show up in the shell and notebooks
Results from confusion_viz will appear in notebooks only
"""
def classification_visualization(y_true,y_pred,y_pred_prob):
    """
    Prints the results of the functions. That's it
    """
    fig = plt.figure()
    fig.tight_layout()
    label1 =classification_report(y_true,y_pred)
    print(label1)
    #fig.add_subplot(3,1,1)
    confusion_viz(y_true,y_pred)
    #fig.add_subplot(3,1,2)
    plt_roc(y_true,y_pred_prob)
    #fig.add_subplot(3,1,3)
    plt_prc(y_true,y_pred_prob)
    
    plt.show();

def confusion_viz(y_true, y_pred):
    """
    Uses labels as given
    Pass y_true,y_pred, same as any sklearn classification problem
    Inspired from code from a Ryan Herr Lambda School Lecture
    """

    y_true = np.array(y_true).ravel()
    labels = unique_labels(y_true,y_pred)
    matrix = confusion_matrix(y_true, y_pred)
    graph = sns.heatmap(matrix, annot=True,
                       fmt=',', linewidths=1,linecolor='grey',
                       square=False,
                       xticklabels=["Predicted\n" + str(i) for i in labels],
                       yticklabels=["Actual\n" + str(i) for i in labels],
                       robust=True,
                       cmap=sns.color_palette("coolwarm"))
    plt.yticks(rotation=0)
    plt.xticks(rotation=0)
    return graph

def plt_prc(y_true, y_pred):
    aps = round(average_precision_score(y_true,y_pred)*100,2)
    a,b,c  = precision_recall_curve(y_true,y_pred)
    plt.figure()
    lw = 2
    plt.plot(a, b, color='darkorange',
             lw=lw, label='Precision Recall curve')
    plt.plot([0, 1], [1, 0], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Precision Recall Curve\nAverage Precision Score = {aps}%')
    plt.legend(loc="lower right")
    plt.show()
    
def plt_roc(y_true,y_pred):
    plt.figure()
    lw = 2
    fpr, tpr, threshold = roc_curve(y_true,y_pred)
    ras = round(roc_auc_score(y_true,y_pred)*100,2)
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve ')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC AUC Curve\nROC AUC Score = {ras}%')
    plt.legend(loc="lower right")
    plt.show()